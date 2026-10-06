from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import CustomerSegmentation, ModelPerformance
from .forms import CustomerSegmentationForm
from .ml_service import CustomerSegmentationService
import json

def home(request):
    """Home page with customer segmentation form"""
    if request.method == 'POST':
        form = CustomerSegmentationForm(request.POST)
        if form.is_valid():
            # Get form data
            customer_data = {
                'Gender': form.cleaned_data['gender'],
                'Ever_Married': form.cleaned_data['ever_married'],
                'Age': form.cleaned_data['age'],
                'Graduated': form.cleaned_data['graduated'],
                'Profession': form.cleaned_data['profession'],
                'Work_Experience': form.cleaned_data['work_experience'],
                'Spending_Score': form.cleaned_data['spending_score'],
                'Family_Size': form.cleaned_data['family_size'],
                'Var_1': form.cleaned_data['var_1'] or 'Cat_4'
            }
            
            # Get prediction method
            prediction_method = request.POST.get('prediction_method', 'random_forest')
            
            # Make prediction
            ml_service = CustomerSegmentationService()
            result = ml_service.predict_segmentation(customer_data, prediction_method)
            
            # Get segment insights
            insights = ml_service.get_segment_insights(result['predicted_segmentation'])
            
            # Save to database
            segmentation = form.save(commit=False)
            segmentation.predicted_segmentation = result['predicted_segmentation']
            segmentation.confidence_score = result['confidence_score']
            segmentation.prediction_method = result['prediction_method']
            segmentation.cluster_id = result.get('cluster_id')
            segmentation.processing_time = result['processing_time']
            segmentation.save()
            
            # Prepare context for result page
            context = {
                'segmentation': segmentation,
                'insights': insights,
                'form': CustomerSegmentationForm(),
            }
            
            messages.success(request, f'Customer segmented successfully as {result["predicted_segmentation"]}!')
            return render(request, 'customer_segmentation/result.html', context)
    else:
        form = CustomerSegmentationForm()
    
    context = {
        'form': form,
        'recent_segmentations': CustomerSegmentation.objects.all()[:5],
    }
    return render(request, 'customer_segmentation/home.html', context)

def sample_data(request):
    """Generate sample data for testing"""
    import random
    
    sample_data = {
        'gender': random.choice(['Male', 'Female']),
        'ever_married': random.choice(['Yes', 'No']),
        'age': random.randint(25, 65),
        'graduated': random.choice(['Yes', 'No']),
        'profession': random.choice([
            'Healthcare', 'Engineer', 'Lawyer', 'Entertainment', 
            'Artist', 'Executive', 'Doctor', 'Homemaker', 'Marketing'
        ]),
        'work_experience': round(random.uniform(1, 20), 1),
        'spending_score': random.choice(['Low', 'Average', 'High']),
        'family_size': round(random.uniform(1, 8), 1),
        'var_1': f'Cat_{random.randint(1, 7)}'
    }
    
    form = CustomerSegmentationForm(initial=sample_data)
    
    context = {
        'form': form,
        'sample_data': sample_data,
    }
    
    return render(request, 'customer_segmentation/home.html', context)

def segmentation_history(request):
    """View all segmentation results with pagination"""
    segmentations = CustomerSegmentation.objects.all()
    paginator = Paginator(segmentations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_count': segmentations.count(),
    }
    return render(request, 'customer_segmentation/history.html', context)

def segmentation_detail(request, pk):
    """View detailed segmentation result"""
    segmentation = CustomerSegmentation.objects.get(pk=pk)
    ml_service = CustomerSegmentationService()
    insights = ml_service.get_segment_insights(segmentation.predicted_segmentation)
    
    context = {
        'segmentation': segmentation,
        'insights': insights,
    }
    return render(request, 'customer_segmentation/detail.html', context)

def analytics_dashboard(request):
    """Analytics dashboard with visualizations"""
    # Get statistics
    total_segmentations = CustomerSegmentation.objects.count()
    segment_distribution = CustomerSegmentation.objects.values('predicted_segmentation').annotate(count=Count('predicted_segmentation'))
    method_distribution = CustomerSegmentation.objects.values('prediction_method').annotate(count=Count('prediction_method'))
    
    # Calculate average confidence scores
    avg_confidence = CustomerSegmentation.objects.aggregate(avg_score=models.Avg('confidence_score'))
    
    # Recent segmentations
    recent_segmentations = CustomerSegmentation.objects.all()[:10]
    
    context = {
        'total_segmentations': total_segmentations,
        'segment_distribution': segment_distribution,
        'method_distribution': method_distribution,
        'avg_confidence': round(avg_confidence['avg_score'] or 0, 3),
        'recent_segmentations': recent_segmentations,
    }
    return render(request, 'customer_segmentation/analytics_simple.html', context)

def model_performance(request):
    """View ML model performance metrics"""
    ml_service = CustomerSegmentationService()
    performance_data = ml_service.get_model_performance()
    
    # Get saved performance records
    performance_records = ModelPerformance.objects.all()
    
    context = {
        'performance_data': performance_data,
        'performance_records': performance_records,
    }
    return render(request, 'customer_segmentation/model_performance.html', context)

def api_predict(request):
    """API endpoint for prediction"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validate required fields
            required_fields = ['gender', 'ever_married', 'age', 'graduated', 'profession', 'spending_score']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Missing required field: {field}'}, status=400)
            
            # Make prediction
            ml_service = CustomerSegmentationService()
            prediction_method = data.get('prediction_method', 'random_forest')
            result = ml_service.predict_segmentation(data, prediction_method)
            
            # Get insights
            insights = ml_service.get_segment_insights(result['predicted_segmentation'])
            
            return JsonResponse({
                'success': True,
                'prediction': result,
                'insights': insights
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

class SegmentationDeleteView(DeleteView):
    """Delete a segmentation record"""
    model = CustomerSegmentation
    template_name = 'customer_segmentation/confirm_delete.html'
    success_url = reverse_lazy('segmentation_history')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Segmentation record deleted successfully!')
        return super().delete(request, *args, **kwargs)

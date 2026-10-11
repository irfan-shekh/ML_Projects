// LapPulse AI - Interactive Engine & UI Controller

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const form = document.getElementById('predictionForm');
  const predictBtn = document.getElementById('predictBtn');
  const priceDisplay = document.getElementById('priceDisplay');
  const currencySymbol = document.getElementById('currencySymbol');
  const priceRange = document.getElementById('priceRange');
  const tierName = document.getElementById('tierName');
  const tierMeterFill = document.getElementById('tierMeterFill');
  const ppiBadge = document.getElementById('ppiBadge');
  const ppiRating = document.getElementById('ppiRating');

  // Inputs
  const companySelect = document.getElementById('company');
  const typeSelect = document.getElementById('type');
  const ramSelect = document.getElementById('ram');
  const weightInput = document.getElementById('weight');
  const weightSlider = document.getElementById('weight_slider');
  const weightBadge = document.getElementById('weightBadge');
  const touchscreenCard = document.getElementById('touchscreenToggle');
  const ipsCard = document.getElementById('ipsToggle');
  const touchscreenInput = document.getElementById('touchscreen');
  const ipsInput = document.getElementById('ips');
  const screenSizeInput = document.getElementById('screen_size');
  const screenSizeSlider = document.getElementById('screen_size_slider');
  const screenSizeBadge = document.getElementById('screenSizeBadge');
  const resolutionSelect = document.getElementById('resolution');
  const cpuSelect = document.getElementById('cpu');
  const hddSelect = document.getElementById('hdd');
  const ssdSelect = document.getElementById('ssd');
  const gpuSelect = document.getElementById('gpu');
  const osSelect = document.getElementById('os');

  // Spec summary display elements
  const specBrand = document.getElementById('specBrand');
  const specType = document.getElementById('specType');
  const specCpu = document.getElementById('specCpu');
  const specRam = document.getElementById('specRam');
  const specStorage = document.getElementById('specStorage');
  const specDisplay = document.getElementById('specDisplay');
  const specGpu = document.getElementById('specGpu');
  const specWeight = document.getElementById('specWeight');
  const featuresTags = document.getElementById('featuresTags');

  // Currencies
  let currentCurrency = 'INR';
  const currencyRates = {
    INR: { symbol: '₹', rate: 1, locale: 'en-IN' },
    USD: { symbol: '$', rate: 0.012, locale: 'en-US' },
    EUR: { symbol: '€', rate: 0.011, locale: 'de-DE' }
  };

  let lastInrPrediction = 71200;
  let lastInrMin = 69700;
  let lastInrMax = 72700;
  let debounceTimer = null;

  // Sync sliders and inputs
  if (weightSlider && weightInput) {
    weightSlider.addEventListener('input', (e) => {
      weightInput.value = parseFloat(e.target.value).toFixed(2);
      if (weightBadge) weightBadge.textContent = `${weightInput.value} kg`;
      updateLiveSummary();
      triggerDebouncedPrediction();
    });

    weightInput.addEventListener('input', (e) => {
      weightSlider.value = e.target.value;
      if (weightBadge) weightBadge.textContent = `${e.target.value} kg`;
      updateLiveSummary();
      triggerDebouncedPrediction();
    });
  }

  if (screenSizeSlider && screenSizeInput) {
    screenSizeSlider.addEventListener('input', (e) => {
      screenSizeInput.value = parseFloat(e.target.value).toFixed(1);
      if (screenSizeBadge) screenSizeBadge.textContent = `${screenSizeInput.value}"`;
      updatePPI();
      updateLiveSummary();
      triggerDebouncedPrediction();
    });

    screenSizeInput.addEventListener('input', (e) => {
      screenSizeSlider.value = e.target.value;
      if (screenSizeBadge) screenSizeBadge.textContent = `${e.target.value}"`;
      updatePPI();
      updateLiveSummary();
      triggerDebouncedPrediction();
    });
  }

  // Toggle Switches (Touchscreen & IPS)
  if (touchscreenCard && touchscreenInput) {
    touchscreenCard.addEventListener('click', () => {
      const isYes = touchscreenInput.value === 'Yes';
      touchscreenInput.value = isYes ? 'No' : 'Yes';
      touchscreenCard.classList.toggle('checked', !isYes);
      updateLiveSummary();
      triggerDebouncedPrediction();
    });
  }

  if (ipsCard && ipsInput) {
    ipsCard.addEventListener('click', () => {
      const isYes = ipsInput.value === 'Yes';
      ipsInput.value = isYes ? 'No' : 'Yes';
      ipsCard.classList.toggle('checked', !isYes);
      updateLiveSummary();
      triggerDebouncedPrediction();
    });
  }

  // Calculate PPI
  function calculatePPI() {
    try {
      const resVal = resolutionSelect.value || '1920x1080';
      const [w, h] = resVal.split('x').map(Number);
      const size = parseFloat(screenSizeInput.value) || 15.6;
      if (size <= 0) return 141;
      return Math.round(Math.sqrt(w * w + h * h) / size);
    } catch {
      return 141;
    }
  }

  function updatePPI() {
    const ppi = calculatePPI();
    if (ppiBadge) ppiBadge.textContent = `${ppi} PPI`;
    if (ppiRating) {
      if (ppi >= 250) {
        ppiRating.textContent = 'Retina Ultra-Sharp';
        ppiRating.style.color = '#34d399';
      } else if (ppi >= 180) {
        ppiRating.textContent = 'Hi-DPI Sharp';
        ppiRating.style.color = '#38bdf8';
      } else if (ppi >= 135) {
        ppiRating.textContent = 'Full HD Standard';
        ppiRating.style.color = '#cbd5e1';
      } else {
        ppiRating.textContent = 'Entry Display';
        ppiRating.style.color = '#94a3b8';
      }
    }
  }

  // Format Price with Currency
  function formatCurrency(amount, curr = currentCurrency) {
    const config = currencyRates[curr];
    const converted = Math.round(amount * config.rate);
    return new Intl.NumberFormat(config.locale).format(converted);
  }

  // Animated Number Counter
  function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      const easeProgress = 1 - Math.pow(1 - progress, 3); // cubic ease out
      const currentVal = Math.floor(easeProgress * (end - start) + start);
      obj.textContent = formatCurrency(currentVal);
      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        obj.textContent = formatCurrency(end);
      }
    };
    window.requestAnimationFrame(step);
  }

  // Update Valuation Display
  function renderValuation(inrPred, inrMin, inrMax, tier = '') {
    lastInrPrediction = inrPred;
    lastInrMin = inrMin;
    lastInrMax = inrMax;

    if (currencySymbol) {
      currencySymbol.textContent = currencyRates[currentCurrency].symbol;
    }

    if (priceDisplay) {
      const prev = parseInt(priceDisplay.textContent.replace(/\D/g, '')) || 0;
      animateValue(priceDisplay, prev, inrPred, 400);
    }

    if (priceRange) {
      const curr = currencyRates[currentCurrency];
      const minFmt = formatCurrency(inrMin);
      const maxFmt = formatCurrency(inrMax);
      priceRange.textContent = `${curr.symbol} ${minFmt} - ${curr.symbol} ${maxFmt}`;
    }

    if (tierName) {
      if (!tier) {
        if (inrPred < 35000) tier = "Budget Friendly";
        else if (inrPred < 65000) tier = "Mid-Range Mainstream";
        else if (inrPred < 110000) tier = "High-End Premium";
        else tier = "Enthusiast / Flagship";
      }
      tierName.textContent = tier;
    }

    if (tierMeterFill) {
      // Scale from 15,000 to 200,000
      const pct = Math.min(100, Math.max(10, ((inrPred - 15000) / 185000) * 100));
      tierMeterFill.style.width = `${pct}%`;
    }
  }

  // Currency Switcher buttons
  document.querySelectorAll('.currency-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.currency-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCurrency = btn.dataset.currency;
      renderValuation(lastInrPrediction, lastInrMin, lastInrMax, tierName?.textContent);
    });
  });

  // Update Live Spec Summary Table & Feature Tags
  function updateLiveSummary() {
    if (specBrand) specBrand.textContent = companySelect.value;
    if (specType) specType.textContent = typeSelect.value;
    if (specCpu) specCpu.textContent = cpuSelect.value;
    if (specRam) specRam.textContent = `${ramSelect.value} GB RAM`;

    const ssdVal = parseInt(ssdSelect.value) || 0;
    const hddVal = parseInt(hddSelect.value) || 0;
    let storageStr = [];
    if (ssdVal > 0) storageStr.push(ssdVal >= 1024 ? `${ssdVal / 1024}TB SSD` : `${ssdVal}GB SSD`);
    if (hddVal > 0) storageStr.push(hddVal >= 1024 ? `${hddVal / 1024}TB HDD` : `${hddVal}GB HDD`);
    if (storageStr.length === 0) storageStr.push('No primary drive');
    if (specStorage) specStorage.textContent = storageStr.join(' + ');

    const ppi = calculatePPI();
    if (specDisplay) specDisplay.textContent = `${screenSizeInput.value}" • ${resolutionSelect.value}`;
    if (specGpu) specGpu.textContent = `${gpuSelect.value} Graphics`;
    if (specWeight) specWeight.textContent = `${weightInput.value} kg (${osSelect.value})`;

    // Dynamic Feature Tags
    if (featuresTags) {
      const tags = [];
      const ram = parseInt(ramSelect.value);
      if (ram >= 16) tags.push('⚡ 16GB+ Heavy Multitasking');
      if (gpuSelect.value === 'Nvidia') tags.push('🎮 Dedicated Nvidia GPU');
      if (gpuSelect.value === 'AMD') tags.push('🔥 Radeon Graphics');
      if (ssdVal >= 512) tags.push('🚀 Ultra-Fast NVMe');
      if (touchscreenInput.value === 'Yes') tags.push('👆 Touchscreen');
      if (ipsInput.value === 'Yes') tags.push('🎨 IPS TrueColor');
      if (parseFloat(weightInput.value) <= 1.4) tags.push('🪶 Featherweight Nomad');
      if (ppi >= 200) tags.push('✨ Retina Level PPI');
      if (osSelect.value === 'Mac') tags.push('🍏 macOS Ecosystem');

      featuresTags.innerHTML = tags.map(t => `<span class="tag-pill">${t}</span>`).join('');
    }
  }

  // Perform AJAX Prediction
  async function performPrediction() {
    if (!predictBtn) return;
    predictBtn.classList.add('loading');

    const payload = {
      company: companySelect.value,
      type: typeSelect.value,
      ram: ramSelect.value,
      weight: weightInput.value,
      touchscreen: touchscreenInput.value,
      ips: ipsInput.value,
      screen_size: screenSizeInput.value,
      resolution: resolutionSelect.value,
      cpu: cpuSelect.value,
      hdd: hddSelect.value,
      ssd: ssdSelect.value,
      gpu: gpuSelect.value,
      os: osSelect.value,
      ajax: 'true'
    };

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error('Prediction API error');
      const data = await response.json();

      if (data.success) {
        renderValuation(data.prediction, data.min_price, data.max_price, data.specs.tier);
      }
    } catch (err) {
      console.warn('Real-time prediction error, will fallback on submit', err);
    } finally {
      predictBtn.classList.remove('loading');
    }
  }

  function triggerDebouncedPrediction() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      performPrediction();
    }, 350);
  }

  // Presets definition
  const presets = {
    gaming: {
      company: 'Asus',
      type: 'Gaming',
      ram: '16',
      weight: '2.40',
      touchscreen: 'No',
      ips: 'Yes',
      screen_size: '15.6',
      resolution: '1920x1080',
      cpu: 'Intel Core i7',
      hdd: '0',
      ssd: '512',
      gpu: 'Nvidia',
      os: 'Windows'
    },
    ultrabook: {
      company: 'Apple',
      type: 'Ultrabook',
      ram: '16',
      weight: '1.25',
      touchscreen: 'No',
      ips: 'Yes',
      screen_size: '13.3',
      resolution: '2560x1600',
      cpu: 'Intel Core i5',
      hdd: '0',
      ssd: '512',
      gpu: 'Intel',
      os: 'Mac'
    },
    student: {
      company: 'HP',
      type: 'Notebook',
      ram: '8',
      weight: '1.75',
      touchscreen: 'No',
      ips: 'No',
      screen_size: '15.6',
      resolution: '1920x1080',
      cpu: 'Intel Core i5',
      hdd: '0',
      ssd: '256',
      gpu: 'Intel',
      os: 'Windows'
    },
    creator: {
      company: 'Dell',
      type: 'Workstation',
      ram: '32',
      weight: '2.00',
      touchscreen: 'Yes',
      ips: 'Yes',
      screen_size: '15.6',
      resolution: '3840x2160',
      cpu: 'Intel Core i7',
      hdd: '0',
      ssd: '1024',
      gpu: 'Nvidia',
      os: 'Windows'
    }
  };

  // Preset click handlers
  document.querySelectorAll('.preset-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const presetKey = chip.dataset.preset;
      const config = presets[presetKey];
      if (!config) return;

      document.querySelectorAll('.preset-chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');

      // Populate form
      setSelectIfOptionExists(companySelect, config.company);
      setSelectIfOptionExists(typeSelect, config.type);
      setSelectIfOptionExists(ramSelect, config.ram);
      setSelectIfOptionExists(cpuSelect, config.cpu);
      setSelectIfOptionExists(gpuSelect, config.gpu);
      setSelectIfOptionExists(osSelect, config.os);
      setSelectIfOptionExists(resolutionSelect, config.resolution);
      setSelectIfOptionExists(ssdSelect, config.ssd);
      setSelectIfOptionExists(hddSelect, config.hdd);

      weightInput.value = config.weight;
      if (weightSlider) weightSlider.value = config.weight;
      if (weightBadge) weightBadge.textContent = `${config.weight} kg`;

      screenSizeInput.value = config.screen_size;
      if (screenSizeSlider) screenSizeSlider.value = config.screen_size;
      if (screenSizeBadge) screenSizeBadge.textContent = `${config.screen_size}"`;

      touchscreenInput.value = config.touchscreen;
      if (touchscreenCard) touchscreenCard.classList.toggle('checked', config.touchscreen === 'Yes');

      ipsInput.value = config.ips;
      if (ipsCard) ipsCard.classList.toggle('checked', config.ips === 'Yes');

      updatePPI();
      updateLiveSummary();
      performPrediction();
      showToast(`Loaded Preset: ${chip.textContent.trim()}`);
    });
  });

  function setSelectIfOptionExists(selectEl, value) {
    if (!selectEl) return;
    for (let opt of selectEl.options) {
      if (opt.value === value) {
        selectEl.value = value;
        return;
      }
    }
  }

  // Toast Notification
  function showToast(msg) {
    let toast = document.getElementById('toastNotice');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toastNotice';
      toast.className = 'toast-notice';
      document.body.appendChild(toast);
    }
    toast.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> <span>${msg}</span>`;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  }

  // Bind change events to all selects
  [companySelect, typeSelect, ramSelect, cpuSelect, gpuSelect, osSelect, resolutionSelect, ssdSelect, hddSelect].forEach(select => {
    if (select) {
      select.addEventListener('change', () => {
        updatePPI();
        updateLiveSummary();
        triggerDebouncedPrediction();
      });
    }
  });

  // Form submit handler
  if (form) {
    form.addEventListener('submit', (e) => {
      // Prevent reload and trigger instant smooth prediction
      e.preventDefault();
      performPrediction();
      showToast('Valuation updated successfully!');
    });
  }

  // Reset defaults button
  const resetBtn = document.getElementById('resetBtn');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      form.reset();
      if (touchscreenCard) touchscreenCard.classList.remove('checked');
      if (touchscreenInput) touchscreenInput.value = 'No';
      if (ipsCard) ipsCard.classList.remove('checked');
      if (ipsInput) ipsInput.value = 'No';
      if (weightSlider) weightSlider.value = 1.5;
      if (weightBadge) weightBadge.textContent = '1.50 kg';
      if (screenSizeSlider) screenSizeSlider.value = 15.6;
      if (screenSizeBadge) screenSizeBadge.textContent = '15.6"';
      updatePPI();
      updateLiveSummary();
      performPrediction();
      showToast('Form reset to default configuration');
    });
  }

  // Keyboard shortcut Ctrl+Enter to predict
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      performPrediction();
    }
  });

  // Initial calculations & sync
  updatePPI();
  updateLiveSummary();
  performPrediction();
});

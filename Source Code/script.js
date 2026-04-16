const fileInput = document.getElementById('fileInput');
const uploadBox = document.getElementById('uploadBox');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const analyzeBtn = document.getElementById('analyzeBtn');
const resetBtn = document.getElementById('resetBtn');
const loading = document.getElementById('loading');
const resultSection = document.getElementById('resultSection');
const resultIcon = document.getElementById('resultIcon');
const resultTitle = document.getElementById('resultTitle');
const confidenceText = document.getElementById('confidenceText');
const confidenceFill = document.getElementById('confidenceFill');
const cameraBtn = document.getElementById('cameraBtn');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');

let currentImageFile = null;
let stream = null;

// ---------- 📁 FILE UPLOAD ----------
uploadBox.addEventListener('click', () => fileInput.click());

uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('dragover');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragover');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) handleFile(files[0]);
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) handleFile(e.target.files[0]);
});

function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please select an image file');
        return;
    }
    
    currentImageFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewSection.style.display = 'block';
        resultSection.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

// ---------- 📷 CAMERA ----------
cameraBtn.addEventListener('click', async () => {
    try {
        if (stream) {
            // Stop camera
            stream.getTracks().forEach(track => track.stop());
            stream = null;
            video.hidden = true;
            cameraBtn.textContent = '📷 Use Camera';
            return;
        }

        stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } });
        video.srcObject = stream;
        video.hidden = false;
        cameraBtn.textContent = '⏹️ Stop Camera';

        // Capture automatically after short delay
        setTimeout(() => capturePhoto(), 1000);
    } catch (error) {
        console.error('Error accessing camera:', error);
        alert('Could not access camera. Please check permissions.');
    }
});

function capturePhoto() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    canvas.toBlob((blob) => {
        const file = new File([blob], 'camera-photo.jpg', { type: 'image/jpeg' });
        handleFile(file);

        // Stop camera after capture
        stream.getTracks().forEach(track => track.stop());
        stream = null;
        video.hidden = true;
        cameraBtn.textContent = '📷 Use Camera';
    }, 'image/jpeg', 0.95);
}

// ---------- 🔍 ANALYZE ----------
analyzeBtn.addEventListener('click', async () => {
    if (!currentImageFile) {
        alert('Please select or capture an image first');
        return;
    }

    loading.style.display = 'block';
    previewSection.style.display = 'none';
    resultSection.style.display = 'none';

    try {
        const formData = new FormData();
        formData.append('image', currentImageFile);

        const response = await fetch('/predict', { method: 'POST', body: formData });
        const result = await response.json();

        if (result.error) throw new Error(result.error);
        displayResult(result);
    } catch (error) {
        console.error('Error:', error);
        alert('Error analyzing image: ' + error.message);
        loading.style.display = 'none';
        previewSection.style.display = 'block';
    }
});

// ---------- 🎯 DISPLAY RESULT ----------
function displayResult(result) {
    loading.style.display = 'none';
    resultSection.style.display = 'block';

    const isWithMask = result.label === 'With Mask';
    const confidence = result.confidence;

    resultTitle.textContent = result.label;
    confidenceText.textContent = `Confidence: ${confidence}%`;

    confidenceFill.style.width = '0%';
    confidenceFill.style.backgroundColor = isWithMask ? '#2e7d32' : '#c62828';

    setTimeout(() => {
        confidenceFill.style.width = `${confidence}%`;
    }, 100);

    // Scroll down to result smoothly
    resultSection.scrollIntoView({ behavior: 'smooth' });
}

// ---------- 🔄 RESET ----------
resetBtn.addEventListener('click', () => {
    currentImageFile = null;
    previewImage.src = '';
    previewSection.style.display = 'none';
    resultSection.style.display = 'none';
    fileInput.value = '';

    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
        video.hidden = true;
        cameraBtn.textContent = '📷 Use Camera';
    }
});

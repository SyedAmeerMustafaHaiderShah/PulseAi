const API_BASE = "http://127.0.0.1:5000/api";

// --- SIGNUP LOGIC ---
const signupForm = document.getElementById('signupForm');
if (signupForm) {
    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const userData = {
            name: document.getElementById('signupName').value,
            email: document.getElementById('signupEmail').value,
            password: document.getElementById('signupPassword').value,
            dob: document.getElementById('signupDOB').value
        };

        try {
            const response = await fetch(`${API_BASE}/signup`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            if (response.ok) {
                alert("Account created! Now please log in.");
                window.location.href = "index.html";
            } else {
                alert("Signup failed. That email might already be registered.");
            }
        } catch (error) {
            alert("Backend server is not running!");
        }
    });
}

// --- LOGIN LOGIC ---
const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;

        try {
            const response = await fetch(`${API_BASE}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (response.ok) {
                // Save user to LocalStorage for use in Dashboard
                localStorage.setItem('pulse_user', JSON.stringify(data.user));
                window.location.href = "dashboard.html";
            } else {
                alert("Invalid email or password.");
            }
        } catch (error) {
            alert("Backend server is not running!");
        }
    });
}
const user = JSON.parse(localStorage.getItem('pulse_user'));
if (user) {
    document.getElementById('userName').innerText = user.name;
} else {
    window.location.href = "index.html"; // Redirect to login if not logged in
}
document.addEventListener('DOMContentLoaded', () => {
    // Core UI Elements
    const chatWindow = document.getElementById('chatWindow');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    
    // Pulse Status Elements
    const moodOrb = document.getElementById('moodOrb');
    const personaDisplay = document.getElementById('personaDisplay');
    const personaEmoji = document.getElementById('personaEmoji');
    const moodTag = document.getElementById('moodTag');
    
    // Progress Bar Elements
    const posValue = document.getElementById('posValue');
    const negValue = document.getElementById('negValue');
    const posBar = document.getElementById('posBar');
    const negBar = document.getElementById('negBar');

    /**
     * Persona Emoji Mapping
     * Maps the persona_name from your EmotionModule to a cute emoji
     */
    const getEmoji = (persona) => {
        const name = persona.toLowerCase();
        if (name.includes('lion')) return '🦁';
        if (name.includes('owl')) return '🦉';
        if (name.includes('batman')) return '🦇';
        if (name.includes('genie')) return '🧞‍♂️';
        if (name.includes('wolf')) return '🐺';
        if (name.includes('cat')) return '🐱';
        if (name.includes('dog')) return '🐶';
        if (name.includes('spider')) return '🕷️';
        if (name.includes('iron man')) return '🚀';
        if (name.includes('superman')) return '🦸‍♂️';
        if (name.includes('joker')) return '🤡';
        if (name.includes('eagle')) return '🦅';
        return '✨'; // Default magic spark
    };

    /**
     * updatePulseUI
     * Syncs the backend metadata with the Frontend attractive elements
     */
    const updatePulseUI = (data) => {
        const neg = data.neg_ratio;
        const pos = data.pos_ratio;
        
        // 1. Update Text Labels
        personaDisplay.innerText = data.persona;
        personaEmoji.innerText = getEmoji(data.persona);
        moodTag.innerText = data.mood;
        posValue.innerText = `${pos}%`;
        negValue.innerText = `${neg}%`;

        // 2. Update Progress Bars (Animated)
        posBar.style.width = `${pos}%`;
        negBar.style.width = `${neg}%`;

        // 3. Update the Glowing Orb & Badge Colors
        if (neg > 70) {
            // CRISIS / STRUGGLE
            moodOrb.style.background = '#f43f5e'; // Rose Red
            moodOrb.style.boxShadow = '0 0 25px #f43f5e';
            moodTag.style.background = '#f43f5e';
        } else if (neg > 30) {
            // BALANCED
            moodOrb.style.background = '#6366f1'; // Indigo
            moodOrb.style.boxShadow = '0 0 25px #6366f1';
            moodTag.style.background = '#6366f1';
        } else {
            // POSITIVE
            moodOrb.style.background = '#10b981'; // Teal Green
            moodOrb.style.boxShadow = '0 0 25px #10b981';
            moodTag.style.background = '#10b981';
        }

        // 4. Add a "Pop" animation to the emoji circle
        const emojiCircle = document.getElementById('personaEmoji');
        emojiCircle.style.transform = 'scale(1.2)';
        setTimeout(() => { emojiCircle.style.transform = 'scale(1)'; }, 300);
    };

    const appendMessage = (role, text) => {
        const div = document.createElement('div');
        div.className = role === 'user' ? 'user-bubble' : 'ai-bubble';
        div.innerText = text;
        chatWindow.appendChild(div);
        
        // Smooth scroll to bottom
        chatWindow.scrollTo({
            top: chatWindow.scrollHeight,
            behavior: 'smooth'
        });
    };

    const sendMessage = async () => {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. GET THE REAL USER DATA FROM LOGIN
    const storedUser = localStorage.getItem('pulse_user');
    if (!storedUser) {
        alert("Session expired. Please login again.");
        window.location.href = "index.html";
        return;
    }
    const user = JSON.parse(storedUser);

    // Show User Message in UI
    appendMessage('user', text);
    userInput.value = '';

    try {
        // 2. SEND THE REAL USER ID TO FLASK
        const response = await fetch('http://127.0.0.1:5000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                message: text,
                user_id: user.id  // <--- THIS IS THE FIX
            })
        });

        const data = await response.json();

        if (data.ai_response) {
            updatePulseUI(data);
            appendMessage('ai', data.ai_response);
        }
    } catch (error) {
        console.error("API Error:", error);
        appendMessage('ai', "⚠️ Server connection failed.");
    }
    };

    // Event Listeners
    sendBtn.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});
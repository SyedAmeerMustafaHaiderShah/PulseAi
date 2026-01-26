Pulse AI — Sentiment Intelligence System
## 📌 Project Overview

Pulse AI is a web-based sentiment intelligence system designed to analyze user-generated text and dynamically influence AI behavior based on detected emotional context.

The system operates as an intermediate processing layer between the user and an AI model. User input is first passed to a custom-built sentiment module, which performs structured preprocessing and emotion analysis. Based on the detected emotional state, the module generates hidden system-level instructions that guide how the AI should respond.

These instructions include mood classification (such as Crisis, Sad, Neutral, or Positive), negativity intensity, and behavioral guidance (for example: empathetic tone, supportive response, or neutral reasoning).

The user interacts normally with the AI and only sees the final response. The internal prompting logic and emotional directives remain completely invisible, allowing emotional intelligence to be injected without exposing system complexity.
## ❗ Problem Statement

Most AI systems treat all user inputs in the same way, focusing only on generating correct answers rather than emotionally appropriate responses. As a result, two AI systems with the same knowledge, same model, and same capabilities may still feel completely different to users.

This can be compared to two hotels offering the same food, same price, and same quality — yet users naturally prefer the one where the staff is more friendly, understanding, and supportive.

Similarly, users tend to trust and engage more with AI systems that respond with emotional awareness, especially during moments of stress, confusion, sadness, or urgency.

Traditional sentiment analysis systems usually stop at labeling text as positive or negative. They do not actively influence how an AI behaves after detecting emotion.

Therefore, there is a need for an intelligent middleware layer that sits between the user and the AI model — one that can understand emotional context and adjust AI behavior dynamically, without exposing internal system instructions to the end user.
## 🧩 Solution Architecture

SentientPulse works as an intelligent middleware layer between the user and any AI model (such as GPT or other LLMs).

Instead of sending raw user input directly to the AI, the system first analyzes emotional context and dynamically modifies AI behavior through hidden system instructions.

### 🔄 Workflow

1. **User Input**
   - The user enters natural language text (message, concern, or query).

2. **Text Preprocessing**
   - Input is cleaned and segmented.
   - Important emotional keywords and linguistic patterns are extracted.

3. **Sentiment & Emotion Analysis**
   - A custom-trained **Naive Bayes Bigram model with TF-IDF vectorization** analyzes the input.
   - The system calculates:
     - Positivity score
     - Negativity score
     - Overall emotional state (Crisis, Struggle, Balanced, Positive)

4. **Persona Mapping Engine**
   - Based on the detected mood, the system selects one of **120 dynamic personas**:
     - 60 animal-based personas
     - 60 pop-culture-inspired personas
   - Each persona carries a predefined behavioral tone.

5. **Hidden System Prompt Generation**
   - The middleware generates internal system-level instructions such as:
     - Communication tone
     - Emotional sensitivity level
     - Response behavior guidelines
   - These instructions remain **completely invisible to the user**.

6. **AI Model Interaction**
   - The final prompt (user input + hidden instructions) is sent to the AI model.
   - The AI responds according to the injected emotional behavior.

7. **Final Response Delivery**
   - The user only sees a natural, empathetic response.
   - All internal logic and system prompts remain hidden.

This architecture allows any AI model to behave in a more emotionally intelligent and human-like manner without modifying the model itself.
## 🚀 Key Features

### 🎭 Emotion-Aware AI Interaction
SentientPulse does not treat every user message the same.  
It understands *how* the user feels before deciding *how* the AI should respond.

---

### 🧠 Custom ML-Based Sentiment Engine
- Built using **Linear Svm **
- TF-IDF vectorization for improved contextual understanding
- Classifies emotions into:
  - Crisis
  - Struggle
  - Balanced
  - Positive

This model is trained and designed manually as part of my AI engineering learning journey.

---

### 🎭 120 Dynamic Personas
- 60 Animal-based emotional personas
- 60 Pop-culture inspired personas
- Each persona represents a unique communication style

This allows the same AI model to behave differently depending on the user’s emotional state — just like humans do.

---

### 🪄 Invisible Prompt Engineering
All emotional logic is injected as **hidden system instructions**.

The user never sees:
- internal prompts
- emotional rules
- behavioral control logic

They only experience a more understanding, friendly, and human-like AI.

---

### 🔗 Plug-and-Play Architecture
- Stateless design
- No database required
- Can be integrated into:
  - Chatbots
  - Mental-health tools
  - Customer support systems
  - Personal AI assistants

Just import the module and connect it with your preferred LLM.

---

### 📊 Developer-Friendly Metadata
Returns internal analytics such as:
- mood label
- positivity/negativity ratios
- persona type

Useful for dashboards, logging, and future AI behavior optimization.
## 🌱 Vision & Motivation

Today, people spend more time with their mobile phones and laptops than with family, friends, or even themselves.

Technology has become a constant companion — but most of the time, it only provides **entertainment**, not **guidance**.

I built SentientPulse with a simple belief:

> If humans are spending so much time with technology,  
> then technology should support them — not ignore how they feel.

Instead of responding with the same tone every time, SentientPulse aims to make AI more emotionally aware — capable of adjusting its behavior based on the user’s mental and emotional state.

This project is not about replacing human connection.  
It is about making digital interaction more responsible, empathetic, and human-centered.
## 🔧 Technical Architecture & Workflow

SentientPulse is designed as a modular middleware system that bridges user input with AI models, injecting emotional intelligence into AI responses. The workflow is fully automated, scalable, and stateless.

### 1. User Input
- Users submit text via the web interface.
- Input can be of any length, informal, or unpunctuated.

### 2. Preprocessing Layer
- Input is segmented using a **15-word batch rule** for handling long or informal text.
- Text normalization includes:
  - Lowercasing
  - Apostrophe correction
  - Stop-word removal
  - Lemmatization
  - Tokenization
- This structured preprocessing ensures consistent feature extraction and model input.

### 3. Feature Engineering
- TF-IDF vectorization with **bigrams** captures contextual sentiment.
- Generates high-dimensional feature vectors that represent the emotional content of the text.

### 4. Sentiment & Emotion Classification
- Custom-trained **Linear SVM** (or Naive Bayes variant in modular engine) classifies the text.
- Outputs include:
  - Negativity/positivity ratio
  - Mood classification: Crisis, Struggle, Balanced, Positive

### 5. Persona Mapping & Hidden Prompt Generation
- Based on the classified mood, selects one of **120 dynamic personas**.
- Generates internal AI instructions:
  - Tone
  - Empathy level
  - Behavioral guidance
- These instructions remain invisible to the user.

### 6. AI Model Integration
- The processed prompt (original user input + hidden instructions) is passed to the AI model (GPT or any LLM).
- The AI model generates a response following the behavioral directives.

### 7. Final Response Delivery
- Users receive a natural, emotionally aware response.
- All internal processing, prompts, and personas remain hidden.

### 8. Scalability & Performance
- Stateless architecture allows for parallel processing of multiple users.
- Modular design enables integration with any AI platform or chatbot.
## 🗂 Project Structure

The project is organized in a modular manner for clarity, scalability, and reusability. Below is an overview:

SentientPulse/
│
├── backend/
│ ├── database/
│ │ └── database.py # Database connection and query management
│ ├── services/
|   |___pulse_service.py
│ │── app.py # Flask application entry point
│ │
│ ├── core_engine/ # Custom AI engine and processing modules
│ │ ├── models/ # Pre-trained ML models
│ │ │ ├── linear_svm_model.pkl
│ │ │ ├── naive_bayes_bigram_model.pkl
│ │ │ ├── tfidf_bigram_vectorizer.pkl
│ │ │ └── tfidf_vectorizer.pkl
│ │ ├── demo.py # Example usage of the engine
│ │ ├── emotion_module.py # Sentiment and emotion analysis logic
│ │ ├── model_accepting_text.py # Handles text input for model inference
│ │ ├── mood_aggregator.py # Aggregates results into mood labels
│ │ ├── persona_registry.py # Maps mood to dynamic personas
│ │ ├── prompt_constructor.py # Builds hidden AI prompts
│ │ ├── sentiment_adapter.py # Connects engine output to AI model
│ │ └── text_processor.py # Preprocessing & feature extraction
│ │
├── frontend/
│ ├── js/
│ │ └── script.js # Frontend JS logic
│ ├── dashboard.html # Main user dashboard
│ ├── index.html # Landing page
│ ├── signup.html # User signup page
│ └── style.css # Frontend styling
│
├── logs/ # System logs
├── .env # Environment variables
├── checksql.py # Utility for checking database connection
├── connectivity_test.py # Network/database connectivity tests
├── imp_info.docx # Project information document
├── test_connection.py # Unit test for database
├── testingotherlogic.py # Utility testing scripts
├── verify_api.py # API testing script
└── verify_full_test.py # End-to-end testing script

👤 Author

Syed Ameer Mustafa Haider Shah
AI Engineering Student | Machine Learning & NLP Enthusiast

📌 Focus Areas:

AI Engineering

Machine Learning

Natural Language Processing

Backend Systems

Intelligent Automation

🔗 GitHub: https://github.com/SyedAmeerMustafaHaiderShah

🔗 LinkedIn: https://www.linkedin.com/in/syedameermustafa/

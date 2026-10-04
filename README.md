# 📧 Smart Email Assistant

An AI-powered **Smart Email Assistant** built with **Python, Streamlit, Gmail IMAP/SMTP, and Google Gemini**. The application can fetch unread Gmail messages, automatically summarize them, generate professional replies using Gemini, allow users to edit the generated response, and send replies directly through Gmail.

---

## 🚀 Features

### 📥 Fetch Unread Emails
- Connects to Gmail using **IMAP**.
- Retrieves emails marked as unread from the inbox.
- Extracts:
  - Sender
  - Recipient
  - Subject
  - Email body
- Displays emails in an interactive Streamlit interface.

### 📝 AI Email Summarization
Each fetched email is automatically summarized using **Google Gemini**.

Instead of reading the complete email, users can quickly understand the main points through an AI-generated summary.

### 🤖 AI Reply Generation
The application can generate a professional reply based on the email content.

Users can:
- Generate a reply.
- Generate another suggested reply.
- Edit the generated response before sending.

### ✉️ Send Email Replies
The application uses Gmail's **SMTP server** to send replies directly from the user's Gmail account.

### 🖥️ Streamlit Interface
The project provides a simple web interface with:
- Expandable email sections
- Email details
- AI summaries
- Reply generation buttons
- Editable reply text areas
- Send buttons

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │      Gmail Inbox     │
                 └──────────┬───────────┘
                            │
                       Gmail IMAP
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Email Fetch Module │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Streamlit UI      │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 │                      │
                 ▼                      ▼
        ┌─────────────────┐    ┌─────────────────┐
        │ Email Summary   │    │ Reply Generator │
        │     Gemini      │    │     Gemini      │
        └─────────────────┘    └────────┬────────┘
                                         │
                                         ▼
                               ┌─────────────────┐
                               │ User Edits Reply│
                               └────────┬────────┘
                                        │
                                        ▼
                               ┌─────────────────┐
                               │   Gmail SMTP    │
                               └────────┬────────┘
                                        │
                                        ▼
                                  📧 Sent Email
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web-based user interface |
| **Gmail IMAP** | Fetch unread emails |
| **Gmail SMTP** | Send email replies |
| **Google Gemini** | Email summarization and reply generation |
| **imaplib** | IMAP communication |
| **smtplib** | SMTP communication |
| **email** | Email parsing and processing |

---

## 📂 Project Structure

```text
smart-email-assistant/
│
├── app.py
├── README.md
├── requirements.txt
│
└── .gitignore
```

> If your Python file has a different name, replace `app.py` with the actual filename.

---

## ⚙️ Requirements

Make sure you have:

- Python 3.9+
- A Gmail account
- Gmail App Password
- Google Gemini API key
- Internet connection

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-email-assistant.git
```

Move into the project directory:

```bash
cd smart-email-assistant
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

Create a `requirements.txt` file containing:

```text
streamlit
google-generativeai
```

Then install:

```bash
pip install -r requirements.txt
```

The following modules are part of Python's standard library and don't need to be installed separately:

```text
imaplib
email
smtplib
email.mime
```

---

# 🔐 Configuration

The application requires three credentials:

```python
GMAIL_EMAIL = "YOUR_GMAIL_EMAIL"
GMAIL_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

### Gmail Email

Enter the Gmail address that the application will use to receive and send emails.

Example:

```python
GMAIL_EMAIL = "example@gmail.com"
```

### Gmail App Password

Do **not** use your normal Gmail password.

Create a **Google App Password** for the Gmail account and use that password in the application.

Example:

```python
GMAIL_APP_PASSWORD = "xxxx xxxx xxxx xxxx"
```

### Gemini API Key

Create a Gemini API key and configure:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

# ▶️ Running the Application

Start Streamlit using:

```bash
streamlit run app.py
```

After starting, Streamlit will provide a local address similar to:

```text
http://localhost:8501
```

Open that address in your browser.

---

# 🖥️ How to Use

### Step 1 — Open the Application

Run:

```bash
streamlit run app.py
```

You will see:

```text
📧 Smart Email Assistant (Gmail + Gemini)
```

---

### Step 2 — Fetch Unread Emails

Click:

```text
📥 Fetch Unread Emails
```

The application connects to Gmail using IMAP and searches for unread messages.

```text
Gmail
  ↓
IMAP
  ↓
UNSEEN emails
  ↓
Email Parser
  ↓
Streamlit
```

---

### Step 3 — Read the Email

Each email appears inside an expandable section containing:

- Sender
- Recipient
- Subject
- Body
- AI-generated summary

---

### Step 4 — Generate a Reply

Click:

```text
Generate Reply
```

Gemini receives the email content and generates a professional response.

---

### Step 5 — Edit the Reply

The generated reply appears inside an editable text box.

You can modify the response before sending it.

---

### Step 6 — Generate Another Reply

If you don't like the first response, click:

```text
Suggest Another Reply
```

A new AI-generated response will replace the previous suggestion.

---

### Step 7 — Send the Reply

After reviewing the response, click:

```text
Send Reply
```

The application connects to Gmail using SMTP and sends the response.

---

# 🔄 Application Workflow

```text
User
 │
 ▼
Streamlit Application
 │
 ▼
Fetch Unread Emails
 │
 ▼
Gmail IMAP
 │
 ▼
Parse Email
 │
 ├── Sender
 ├── Recipient
 ├── Subject
 └── Body
       │
       ▼
   Gemini AI
       │
       ├───────────────┐
       ▼               ▼
   Summarization   Reply Generation
                       │
                       ▼
                  User Review
                       │
                       ▼
                   Edit Reply
                       │
                       ▼
                   Gmail SMTP
                       │
                       ▼
                  Send Email
```

---

# 🧠 AI Components

The project currently uses Google Gemini for two primary tasks.

## 1. Email Summarization

The email body is sent to Gemini with a prompt similar to:

```text
Summarize this email:

<email content>
```

Gemini generates a concise summary that is displayed in the UI.

---

## 2. Reply Generation

The email body is provided to Gemini with a prompt similar to:

```text
Write a professional reply to this email:

<email content>
```

Gemini generates a suggested response.

The user remains in control and can modify the response before sending it.

---

# 🔒 Security Considerations

**Never upload your credentials to GitHub.**

Do not commit:

```text
GMAIL_EMAIL
GMAIL_APP_PASSWORD
GEMINI_API_KEY
```

For example, avoid committing:

```python
GEMINI_API_KEY = "AIza..."
```

Instead, use environment variables or Streamlit secrets.

A recommended approach is:

```text
.streamlit/
└── secrets.toml
```

Example:

```toml
GMAIL_EMAIL = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_app_password"
GEMINI_API_KEY = "your_gemini_api_key"
```

Then access them in Python using:

```python
GMAIL_EMAIL = st.secrets["GMAIL_EMAIL"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
```

Add this to `.gitignore`:

```text
.streamlit/secrets.toml
venv/
__pycache__/
.env
```

---

# ⚠️ Important Limitations

### 1. Only Unread Emails Are Retrieved

The application currently searches using:

```python
mail.search(None, "UNSEEN")
```

Therefore, only emails marked as unread are fetched.

---

### 2. Plain-Text Emails

The current implementation primarily extracts:

```text
text/plain
```

HTML-only emails may not be processed correctly.

---

### 3. AI-Generated Responses

Gemini-generated replies should always be reviewed before sending.

AI-generated content can occasionally:

- Misinterpret the email
- Produce incorrect information
- Use an inappropriate tone
- Miss important context

The application therefore allows the user to edit the reply before sending it.

---

### 4. API Usage

Every summarization and reply-generation request consumes Gemini API usage.

Large emails can also result in larger API requests.

---

# 🚀 Future Improvements

The project can be extended into a more advanced AI email assistant.

### 🔹 Smart Email Classification

Automatically classify emails as:

```text
Important
Work
College
Personal
Promotional
Spam
```

### 🔹 Priority Detection

Automatically identify urgent emails.

Example:

```text
🔥 High Priority
📌 Important
📨 Normal
```

### 🔹 Better Reply Generation

Allow users to select a response style:

```text
Professional
Friendly
Short
Detailed
Formal
Casual
```

### 🔹 Email Search

Allow users to search emails by:

- Sender
- Subject
- Keywords
- Date
- Category

### 🔹 Attachment Processing

Add support for:

```text
PDF
DOCX
Images
Excel
```

The assistant could summarize important attachments along with the email.

### 🔹 Conversation Context

Instead of generating replies from only the latest email, the system could retrieve previous messages from the email thread to generate context-aware replies.

### 🔹 RAG-Based Email Assistant

A Retrieval-Augmented Generation system could be added so the assistant can use:

```text
Previous Emails
      +
Personal Knowledge Base
      +
College/Work Documents
      +
Current Email
      ↓
     RAG
      ↓
   Gemini
      ↓
Context-Aware Reply
```

### 🔹 Automatic Email Triage

The system could automatically process incoming emails and create:

```text
Email
 ↓
Classification
 ↓
Priority Detection
 ↓
Summarization
 ↓
Action Detection
 ↓
Suggested Response
```

---

# 📊 Example

### Incoming Email

```text
Subject: Interview Schedule

Hello Joseph,

Your technical interview has been scheduled for
Monday at 10:00 AM.

Please confirm your availability.

Regards,
HR Team
```

### AI Summary

```text
The HR team has scheduled your technical interview
for Monday at 10:00 AM and is requesting confirmation.
```

### AI Suggested Reply

```text
Dear HR Team,

Thank you for the update. I confirm my availability
for the technical interview scheduled for Monday at
10:00 AM.

Best regards,
Joseph
```

The user can edit the response before sending it.

---

# 🎯 Project Objective

The main objective of this project is to reduce the time required to manage emails by combining traditional email protocols with generative AI.

Instead of manually:

```text
Open Email
     ↓
Read Entire Email
     ↓
Understand Email
     ↓
Write Reply
     ↓
Send
```

the system provides:

```text
Fetch Email
     ↓
AI Summary
     ↓
AI Reply
     ↓
User Review
     ↓
Send
```

This creates a faster and more convenient email-management workflow while keeping the user responsible for the final response.

---

# 📌 Project Highlights

- ✅ Gmail integration
- ✅ IMAP email retrieval
- ✅ SMTP email sending
- ✅ Unread email detection
- ✅ Gemini-powered summarization
- ✅ AI reply generation
- ✅ Multiple reply suggestions
- ✅ Editable AI responses
- ✅ Streamlit web interface
- ✅ User-controlled email sending
- ✅ Extensible architecture for future AI features

---

# 👨‍💻 Author

**Joseph Mathew**

Engineering Student  
Interested in **AI/ML, Generative AI, Python, and Software Development**

---

# 📄 License

This project is intended for educational and development purposes.

You may modify and extend the project according to your requirements.

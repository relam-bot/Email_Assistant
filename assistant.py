import streamlit as st
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai

# ==========================
# CONFIGURATION
# ==========================
GMAIL_EMAIL = "relam4349@gmail.com"
GMAIL_APP_PASSWORD = "iepx wbnt uyqy bypc"  # Gmail App Password
GEMINI_API_KEY = "AIzaSyChvNEMy9-GrXdapqDPU2SWkoObCAuznaw"

# IMAP & SMTP
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


# ==========================
# FETCH UNREAD EMAILS
# ==========================
def fetch_unread_emails():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        mail.select("inbox")

        status, data = mail.search(None, "UNSEEN")
        email_ids = data[0].split()

        emails = []
        for eid in email_ids:
            status, msg_data = mail.fetch(eid, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg["subject"]
            from_email = msg["from"]
            to_email = msg["to"]
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode(errors="ignore")
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            # Auto-summarize here
            summary = summarize_email(body)

            emails.append({
                "id": eid.decode(),
                "subject": subject,
                "from": from_email,
                "to": to_email,
                "body": body,
                "summary": summary
            })

        mail.logout()
        return emails

    except Exception as e:
        st.error(f"Error fetching emails: {e}")
        return []


# ==========================
# SUMMARIZE EMAIL
# ==========================
def summarize_email(email_body):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Summarize this email:\n\n{email_body}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error summarizing: {e}"


# ==========================
# GENERATE REPLY
# ==========================
def generate_reply(email_body):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a professional reply to this email:\n\n{email_body}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating reply: {e}"


# ==========================
# SEND EMAIL
# ==========================
def send_email(to_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["From"] = GMAIL_EMAIL
        msg["To"] = to_email
        msg["Subject"] = f"Re: {subject}"

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_EMAIL, to_email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False


# ==========================
# STREAMLIT UI
# ==========================
def run_ui():
    st.title("📧 Smart Email Assistant (Gmail + Gemini)")

    if st.button("📥 Fetch Unread Emails"):
        st.session_state.emails = fetch_unread_emails()
        st.session_state.replies = {}

    if "emails" in st.session_state and st.session_state.emails:
        for idx, mail_data in enumerate(st.session_state.emails):
            with st.expander(f"📩 {mail_data['subject']} — From: {mail_data['from']}"):
                st.write("**From:**", mail_data["from"])
                st.write("**To:**", mail_data["to"])
                st.write("**Body:**", mail_data["body"])
                st.write("### 📝 Summary:")
                st.write(mail_data["summary"])

                # Generate Reply
                if st.button(f"Generate Reply {idx}"):
                    reply_text = generate_reply(mail_data["body"])
                    st.session_state.replies[idx] = reply_text

                # Suggest Another Reply
                if st.button(f"Suggest Another Reply {idx}"):
                    new_reply = generate_reply(mail_data["body"])
                    st.session_state.replies[idx] = new_reply

                # Show Reply if Exists
                if idx in st.session_state.get("replies", {}):
                    st.write("### 💬 Suggested Reply:")
                    reply_text = st.text_area(
                        f"Edit Reply {idx}",
                        value=st.session_state.replies[idx],
                        height=150
                    )
                    st.session_state.replies[idx] = reply_text

                    # Send Button
                    if st.button(f"Send Reply {idx}"):
                        if send_email(mail_data["from"], mail_data["subject"], reply_text):
                            st.success("✅ Reply sent successfully!")


if __name__ == "__main__":
    run_ui()

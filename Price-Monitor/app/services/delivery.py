from pathlib import Path

def send_email(attachment_path):
    import smtplib
    from email.message import EmailMessage
    from app.core.config import ACCOUNT, PASS_WORD

    subject = "Books Price Monitor"
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = ACCOUNT
    msg["To"] = ACCOUNT

    try:
        attachment_path = Path(attachment_path)
        if not attachment_path.exists():
            raise FileNotFoundError(f"Attachment not found: {attachment_path}")

        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="csv",
                filename=attachment_path.name
            )
    except Exception as e:
        print(f"Error attaching file: {e}")
        return False

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(ACCOUNT, PASS_WORD)
            s.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your ACCOUNT/PASS_WORD.")
    except Exception as e:
        print(f"Error sending email: {e}")
    return False


def update_sheet(df):
    import gspread
    from google.oauth2.service_account import Credentials
    from app.core.config import CREDENTIALS, SHEET_ID
    
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    try:
        creds = Credentials.from_service_account_file(CREDENTIALS, scopes=scopes)
        client = gspread.authorize(creds)
    except FileNotFoundError:
        print(f"Credentials file not found: {CREDENTIALS}")
        return False
    except Exception as e:
        print(f"Error authorizing Google Sheets client: {e}")
        return False

    sheet_id = SHEET_ID

    try:
        workbook = client.open_by_key(sheet_id)
        sheet = workbook.worksheet("Página1")
        sheet.clear()
        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        return True
    except gspread.exceptions.WorksheetNotFound:
        print("Worksheet 'Página1' not found.")
    except Exception as e:
        print(f"Error updating sheet: {e}")
    return False

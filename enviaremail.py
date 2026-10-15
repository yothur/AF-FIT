import smtplib
from email.message import EmailMessage
import os
import smtplib
from datetime import date
from html import escape
from repository.usuariodao import UsuarioDAO
from dotenv import load_dotenv

load_dotenv()
REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("EMAIL_SENHA_APP")
DIAS_ANTES = 3

def enviaremail(nome, destino, vencimento):
    corpo_email = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body style="margin: 0; padding: 0; background-color: #f4f4f5; font-family: Arial, sans-serif; -webkit-font-smoothing: antialiased;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; margin: 30px auto; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
            <tr>
                <td align="center" style="background-color: #111827; padding: 32px 20px;">
                    <h1 style="margin: 0; font-size: 42px; font-weight: 900; letter-spacing: -1px; line-height: 1;">
                        <span style="color: #f3f4f6;">AF</span><span style="color: #ef4444;">FIT</span>
                    </h1>
                </td>
            </tr>
            <tr>
                <td style="padding: 36px 32px; color: #374151;">
                    <p style="font-size: 18px; font-weight: bold; color: #111827; margin-top: 0; margin-bottom: 16px;">
                        Olá, {escape(nome)}!
                    </p>
                    <p style="font-size: 15px; line-height: 1.6; color: #4b5563; margin-bottom: 24px;">
                        Aqui quem fala é a equipe da <strong style="color: #111827;">AFFIT</strong>. Passando para avisar que o seu plano está perto de vencer!
                    </p>
                    <div style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 16px 20px; border-radius: 6px; margin-bottom: 28px;">
                        <p style="margin: 0; font-size: 14px; color: #991b1b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Data de Vencimento</p>
                        <p style="margin: 6px 0 0 0; font-size: 22px; font-weight: bold; color: #b91c1c;">
                            {vencimento:%d/%m/%Y}
                        </p>
                    </div>
                    <p style="font-size: 14px; line-height: 1.5; color: #6b7280; margin-bottom: 32px;">
                        Para garantir que seu acesso aos treinos e benefícios continue sem interrupções, renove o seu plano antes do vencimento.
                    </p>
                </td>
            </tr>
            <tr>
                <td align="center" style="background-color: #f9fafb; padding: 20px; border-top: 1px solid #e5e7eb; color: #9ca3af; font-size: 12px;">
                    <p style="margin: 0;">© {date.today().year} AFFIT. Todos os direitos reservados.</p>
                    <p style="margin: 4px 0 0 0;">Este é um e-mail automático, por favor não responda.</p>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    msg = EmailMessage()
    msg['Subject'] = 'Vencimento do seu plano'
    msg['From'] = REMETENTE
    msg['To'] = destino
    msg.set_content(corpo_email, subtype='html')

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(REMETENTE, SENHA_APP)
        s.send_message(msg)


def avisar_planos_a_vencer():
    hoje = date.today()
    for u in UsuarioDAO.listar_usuarios():
        if u.is_admin or not u.plano:
            continue

        vencimento = u.plano.vencimento     
        if hasattr(vencimento, 'date'):           
            vencimento = vencimento.date()

        if (vencimento - hoje).days == DIAS_ANTES:
            enviaremail(u.nome, u.email, vencimento)

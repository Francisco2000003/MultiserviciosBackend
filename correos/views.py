# correos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from email.message import EmailMessage
import smtplib

class ContactAPIView(APIView):
    authentication_classes = []   # público
    permission_classes = []       # público

    def post(self, request):
        # Datos del formulario
        nombre = (request.data.get("nombre") or "").strip()
        email  = (request.data.get("email") or "").strip()
        mensaje= (request.data.get("mensaje") or "").strip()

        # Validación mínima
        errors = {}
        if not nombre:
            errors["nombre"] = "Ingresa tu nombre"
        if "@" not in email or "." not in email:
            errors["email"] = "Correo inválido"
        if len(mensaje) < 10:
            errors["mensaje"] = "Describe el problema o servicio (mínimo 10 caracteres)"
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        # Configuración directa (TU CORREO Y APP PASSWORD)
        remitente = "franciscophdz03@gmail.com"
        destinatario = "oswaldophdz03@gmail.com"  # o el mismo remitente si quieres recibir ahí
        app_password = "ovdy tcit rryi scfx"  # ⚠️ generado en Google

        # Redacción del correo
        subject = f"[MSVO] Nuevo contacto: {nombre}"
        body = (
            "Has recibido una nueva solicitud desde el formulario de contacto.\n\n"
            f"• Nombre: {nombre}\n"
            f"• Correo: {email}\n\n"
            "• Descripción del problema o servicio solicitado:\n"
            f"{mensaje}\n"
        )

        try:
            email = EmailMessage()
            email["From"] = remitente
            email["To"] = destinatario
            email["Subject"] = subject
            email.set_content(body)

            smtp = smtplib.SMTP_SSL('smtp.gmail.com')
            smtp.login(remitente, app_password)
            smtp.sendmail(remitente, destinatario, email.as_string())
            smtp.quit()


        except Exception as e:
            return Response(
                {"ok": False, "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"ok": True, "message": "Mensaje enviado correctamente"})


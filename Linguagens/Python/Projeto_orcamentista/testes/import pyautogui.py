import pytesseract
import pyautogui

# Capturar a tela inteira
screenshot = pyautogui.screenshot()

# Salvar a captura em um arquivo de imagem
screenshot.save('screenshot.png')

# Reconhecimento óptico de caracteres (OCR) para converter a imagem em texto
# É necessário ter a biblioteca pytesseract instalada (pip install pytesseract)

# Configurar o caminho para o executável do Tesseract OCR (pode variar dependendo do sistema operacional)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ler o texto da imagem
text = pytesseract.image_to_string(screenshot)

# Exibir o texto capturado
print(text)

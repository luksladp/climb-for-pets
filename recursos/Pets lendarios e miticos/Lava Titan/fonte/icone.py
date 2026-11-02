# Ícone 128 px do Lava Titan a partir do render "icone" (fundo transparente): recorta, centraliza e põe
# contorno escuro fino + luz de recorte quente leve, fundo transparente, ~9% de margem.
import sys
from PIL import Image, ImageEnhance, ImageFilter
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA'); im = im.crop(im.getbbox())
rgb = ImageEnhance.Contrast(ImageEnhance.Brightness(im.convert('RGB')).enhance(1.12)).enhance(1.3)   # mais contraste
im = Image.merge('RGBA', (*rgb.split(), im.split()[3]))
w, h = im.size; S = max(w, h); c = Image.new('RGBA', (S, S), (0, 0, 0, 0)); c.paste(im, ((S - w) // 2, (S - h) // 2))
c = c.resize((100, 100), Image.LANCZOS); base = Image.new('RGBA', (128, 128), (0, 0, 0, 0)); base.paste(c, (14, 14))   # ~9% de margem
a = base.split()[3]
dark = a.filter(ImageFilter.MaxFilter(3)); warm = a.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.0))
out = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
out.alpha_composite(Image.merge('RGBA', (*Image.new('RGB', (128, 128), (255, 140, 50)).split(), warm.point(lambda v: v * 0.55))))
out.alpha_composite(Image.merge('RGBA', (*Image.new('RGB', (128, 128), (22, 16, 24)).split(), dark)))
out.alpha_composite(base); out.save(dst)

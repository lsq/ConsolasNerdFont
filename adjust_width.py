import fontforge

#font = fontforge.open("orig.ttf")
font_path = "./orig.ttf"
target_width = 1024 # 目标宽度

def bound(glyph):
    (left, bottom, right, top) = glyph.boundingBox()
    print(f"left, bottom, right, top: {left, bottom, right, top}")

def fixAnchor(glyph, scale_factor, offset):
    for anchor in glyph.anchorPoints:
        anchor.x = (anchor.x * scale_factor) + offset

def adust_glyph_width(glyph):
    if glyph.width > 0:  # 跳过空白字形
        bound(glyph)
        scale_factor = target_width / glyph.width
        # offset = (1 - scale_factor) * glyph.width / 2 # 水平居中补偿
        offset = 0 # 水平居中补偿
        # 说明：
        # 该方法接受一个6元组作为变换矩阵参数，格式为：
        # (a, b, c, d, e, f)
        # 对应二维仿射变换矩阵：
        # [ a  b  0 ]
        # [ c  d  0 ]
        # [ e  f  1 ]
        #
        # 其中：
        #     a和d控制X/Y轴缩放
        #     b和c控制倾斜
        #     e和f控制平移
        glyph.transform((scale_factor, 0, 0, scale_factor, offset, 0))  # 水平缩放
        print(f'width: {glyph.width}')
        # bound(glyph)
        # glyph.width = target_width  # 强制设置宽度
        # bound(glyph)

font = fontforge.open(font_path)
# 测试字母b、c
# chars_to_adust = ["b", "c"]
# for char in chars_to_adust:
    # glyph = font[char]

# 全部字体
for glyph in font.glyphs():
    adust_glyph_width(glyph)


font.generate("new_font_width_500.ttf")
font.close()


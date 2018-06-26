# encoding: utf-8
import media
import fresh_tomatoes

title = "علي وكتاب - الفارق البسيط The Slight Edge"
story_line = """أول حلقات برنامج علي وكتاب مع كتاب 
The Slight Edge .. أو الفارق البسيط
مع هذا الكتاب نتعلم لماذا يفشل الناس في تطبيق ما يعرفونه من معرفة مفيدة .. وما الحل الأمثل للتغيير وتحقيق النجاح."""
img_url = "http://img.youtube.com/vi/biCRsdst958/0.jpg"
youtube_url = "https://www.youtube.com/watch?v=biCRsdst958&list=PLDN8vU_ZehsW7bFxs0yG5yNImjueqo3UY&index=2"
slight_edge = media.Movie(title, story_line, img_url, youtube_url)

# print slight_edge.story_line
# slight_edge.show_trailer()

title = "علي وكتاب - حل لغز التسويف Solving The Procrastination Puzzle"
story_line = """كتاب حل لغز التسويف المماطلة .. هنتعرف من خلاله على أسباب التسويف ومخاطره وكيفية علاجه."""
img_url = "http://img.youtube.com/vi/22CW76-SARA/0.jpg"
youtube_url = "https://www.youtube.com/watch?v=22CW76-SARA&index=3&list=PLDN8vU_ZehsW7bFxs0yG5yNImjueqo3UY"
procrastination_puzzle = media.Movie(title, story_line, img_url, youtube_url)


title = "علي وكتاب - قوة الإرادة Will Power"
story_line = """نتعرف في حلقة اليوم على ما هي قوة الإرادة وما طبيعتها وكيف تقوي عضلة قوة الإرادة عندك
سنتعرف على تأثير المشاعر والبيئة المحيطة على قوة الإرادة 
سنتكلم عن بناء العادات وحرق السفن والتنفس بعمق
ستتعلم كيف تمتلك قوة الإرادة لتحقيق النجاح"""
img_url = "http://img.youtube.com/vi/THnrunRXYss/0.jpg"
youtube_url = "https://www.youtube.com/watch?v=THnrunRXYss&index=6&list=PLDN8vU_ZehsW7bFxs0yG5yNImjueqo3UY"
will_power = media.Movie(title, story_line, img_url, youtube_url)

title = "علي وكتاب - العمل العميق Deep Work"
story_line = """مع كتاب اليوم سنتعلم أهمية وكيفية العمل بتركيز لتحقيق إنتاجية أكبر في وقت أقل"""
img_url = "http://img.youtube.com/vi/o1wHtClg6OQ/0.jpg"
youtube_url = "https://www.youtube.com/watch?v=o1wHtClg6OQ&index=9&list=PLDN8vU_ZehsW7bFxs0yG5yNImjueqo3UY"
deep_work = media.Movie(title, story_line, img_url, youtube_url)

title = "خمس كتب في خمس دقائق! - علي وكتاب"
story_line = """في هذا الفيديو نعرض خمس كتب في خمس دقائق .. لكن لماذا يا ترى؟"""
img_url = "http://img.youtube.com/vi/FQRMYuIzNjA/0.jpg"
youtube_url = "https://www.youtube.com/watch?v=FQRMYuIzNjA&index=16&list=PLDN8vU_ZehsW7bFxs0yG5yNImjueqo3UY"
five_books = media.Movie(title, story_line, img_url, youtube_url)


movies = [slight_edge, procrastination_puzzle, will_power, deep_work, five_books]
fresh_tomatoes.open_movies_page(movies)

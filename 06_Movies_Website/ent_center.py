# encoding: utf-8
import media

title = "حتة حكمة - حاول مرة كمان"
story_line = """معظمنا لما بنبدأ مشروع جديد أو بنحاول نكتسب  مهارة أو عادة جديدة في حياتنا  
بيكون عندنا أمل - أو وهم - إن كل شيء هيمشي حسب الخطة الموضوعة
 وبأننا هننجح بدون معوقات ومن المحاولة الأولى!"""
img_url = "img_url"
youtube_url = "https://www.youtube.com/watch?v=lUB89q_FIug"

hikma = media.Movie(title, story_line, img_url, youtube_url)

print hikma.story_line
hikma.show_trailer()

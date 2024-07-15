def create_youtube_video(title, description):
	Youtube_video  = {"Title" : title, "Description" : description, "Likes" : 0, "Dislikes" : 0, "Comments" : {"username" : {}}}
	return Youtube_video
def like(Youtube_video):
	Youtube_video["Likes"] +=1
	return Youtube_video
def dislike(Youtube_video):
	Youtube_video["Dislikes"] +=1
	return Youtube_video
def add_comment(Youtube_video, username, comment_text):
	Youtube_video["Comments"] = username
	Youtube_video["Comments"][username] = [comment_text]
	return Youtube_video
Abo_elis_ytvid = create_youtube_video("Prank on Abo Sami", "It was amazing")
Abo_elis_ytvid = like(Abo_elis_ytvid)
while Abo_elis_ytvid["Dislikes"] < 69:
	Abo_elis_ytvid = dislike(Abo_elis_ytvid)
print(Abo_elis_ytvid)

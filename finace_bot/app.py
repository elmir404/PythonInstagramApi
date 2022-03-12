from calendar import c
import instaloader

L = instaloader.Instaloader() 
L.login("","")
a=str(input("hedef hesabi daxil edin:"))
profile = instaloader.Profile.from_username(L.context, a)
 
print(profile.get_posts())
i=0
code=str(input("post kodunu daxil edin:"))

for post in profile.get_posts():
    print("post id,",i+1)
    print(post.shortcode)
    if post.shortcode==code:
        post_likes = post.get_likes()
        post_comments = post.get_comments()

    

    
        print("likes-------------------")
        with open('likes.txt','w') as f:
            for likee in post_likes:
                print(str(likee.biography))
                f.write(str(likee.biography))
                f.write('\n')

        print("commentler------------------")
        with open('comments.txt','w') as f:

            for comment in post_comments:
                f.write(str(comment.owner.username))
                f.write('\n')
                print(comment.owner.username)

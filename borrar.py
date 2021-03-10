
videos=[{"video_id":1},{"video_id":1},{"video_id":2},{"video_id":3},{"video_id":4} ]

def masrepetido(videos):
    i=0
    contador=1
    videoconmasrep=0
    while i < len(videos)-1:
        video1 =videos[i]
        video2 =videos[i+1]
        if video1["video_id"] == video2["video_id"]:
            contador+= 1
        else:
            if contador > videoconmasrep:
                videoconmasrep = contador
        i+=1
        video=videos[i]
    return (video,videoconmasrep)
print(masrepetido(videos))
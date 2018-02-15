import requests
hello = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCpNooCUr-Q01rjgqxzjvztg&key=AIzaSyC4ucWTSN3s7d4KrqJ9ZOYZ-ezvzwTSGsg";
request = requests.get(hello);
reallist = ['\"','{','}','\n',']']
data = request.content;

sdata = data;
for character in reallist:
        sdata = sdata.replace(character,'');
sdata = sdata.split(',');
def get_channel_id():
    channel_id = sdata[6].replace('id: ','');
    channel_id = channel_id.replace(' ','');
    return channel_id;

def get_viewcount():
    viewcount = sdata[7].split(':');
    viewcount = viewcount[2].replace(' ','');
    return viewcount;

def get_subscribers():
    subscribers = sdata[9].split(':');
    subscribers = subscribers[1].replace(' ','');
    return subscribers;

def get_videoCount():
    videoCount = sdata[11].split(':');
    videoCount = videoCount[1].replace(' ','');
    return videoCount





channel_id = get_channel_id();
viewcount = get_viewcount();
subscribers = get_subscribers();
videoCount = get_videoCount();

info_list = [channel_id,viewcount,videoCount,subscribers];
info_list = "\n".join(info_list);
channel_id_title = 'Channel ID: ' + channel_id;
view_count_title = 'Views: ' + viewcount;
subscribers_title = 'Subscribers: ' + subscribers;
video_Count_title = 'Videos: ' + videoCount;

info_list_title = [channel_id_title,view_count_title,subscribers_title,video_Count_title];
info_list_title = '\n'.join(info_list_title);

def writetofile():
    fh = open("Channel_Info.txt", "w")
    fh.writelines(str(info_list_title));
    fh.close()

writetofile();

print(info_list)

print('Channel ID: ' + channel_id + '\n' + 'Views: ' + viewcount + '\n' + 'Videos: ' + videoCount + '\n' + 'Subscribers; ' + subscribers);


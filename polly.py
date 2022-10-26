# GUI for T2S Converter
import tkinter as tk
from urllib import response
import boto3

print(boto3.__version__)
import os
import sys
import tempfile
import gettempdir
from contextlib import closing
root=tk.Tk()
root.geometry("400x250")
root.title("T2S-con Amazon polly")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.session(profile_name='sirisha')
    client=aws_mag_con.client(service_name='polly',region_name='us-east-1')
    result=textExample.get("1.0","end")
    print(result)
    response=client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3',Text=result,Engine='neural')
    print(response)
    if "AudoStream" in response:
        with closing(response['AudioStream']) as stream:
            output=os.path.join(gettempdir(), "speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("could not find the stream")
        sys.exit(-1)
    if sys.platform=='apple M1':
        os.startfile(output)
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()

root.mainloop()

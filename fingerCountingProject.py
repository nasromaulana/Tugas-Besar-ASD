import cv2 #import library untuk image prosessing
import os #import library untuk fungsi yang berinteraksi dengan os untuk fps
import time #modul untuk time
import handTrackingModule as htm #import file handTrackingModule dijadikan library

def Nomor(ar): #Fungsi buat mendapatkan nomor
    s=""
    for i in ar:
       s+=str(ar[i])
    if(s=="00000"):
        return (10)
    elif(s=="01000"):
        return(1)
    elif(s=="01100"):
        return(2) 
    elif(s=="01110"):
        return(3)
    elif(s=="01111"):
        return(4)
    elif(s=="11111"):
        return(5) 
    elif(s=="01001"):
        return(6)
    elif(s=="01101"):
        return(7) 
    elif(s=="01011"):
        return(8) 
    elif(s=="01010"):
        return(9)      
 
wcam,hcam=640, 480
cap=cv2.VideoCapture(0)
#fungsi perpustakaan openCV untuk pemrosesan dengan menangkap melalui webcam internal "(0)"
cap.set(3,wcam) #ukuran tampilan kamera
cap.set(4,hcam)
pTime=0 #deklarasi variabel pTime (previous time)
detector = htm.handDetector(detectionCon=0.75) # instansiasi class

while True:
    success,img = cap.read() #membuat/membaca frame kamera
    img = detector.findHands(img, draw=True ) #mendeteksi tangan pada kamera
    lmList=detector.findPosition(img,draw=False) #mendeteksi koordinat tiap titik pada jari tangan
    tipId=[4,8,12,16,20] #mengambil titik ujung ditiap jari
    if(len(lmList)!=0): #mengecek kalo ada tangan di kamera lalu
        jari=[]
        #jempol
        if(lmList[tipId[0]][1]>lmList[tipId[0]-1][1]): #mengecek jempol membuka atau menutup, lmList[4][1] > lmList[3][1], [1] merupakan sumbu x
                jari.append(1) #klo sesuai kondisi diatas append(1)
        else :
                jari.append(0) #klo sesuai kondisi diatas append(0)
        #4 jari lain
        for id in range(1,5):
            
            if(lmList[tipId[id]][2]<lmList[tipId[id]-2][2]):
                jari.append(1)
            else :
                jari.append(0)
        print(jari)
           
        cv2.rectangle(img,(20,255),(170,425),(69,69,69),cv2.FILLED)  
        #cv2.rectangle(image, start_point, end_point, color, thickness)
        #membuat kotak tempat angka
        cv2.putText(img,str(Nomor(jari)),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(0,0,0),20)  
        #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        #membuat tampilan angka
  
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
    #membuat tampilan fps
    cv2.imshow("image",img)
    #cv2.imshow(window_name, image)
    #menampilkan hasil kamera dalam window bernama image

    if(cv2.waitKey(1) & 0xFF== ord('q')): #delay selama 1 milisecond dalam vidio 
        break #pencet q = keluar


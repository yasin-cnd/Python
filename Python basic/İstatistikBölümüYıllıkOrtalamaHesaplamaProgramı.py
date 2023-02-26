sınıfseçiniz=int(input("sınıf seçiniz 1/2/3/4 : "))
if sınıfseçiniz==1: ##sınıfın seçilmesi

    dönemseçiniz=str(input("dönem güz/bahar: "))
    if dönemseçiniz=="güz": ## dönemin seçilmesi
       
        dersSeçiniz=str(input("ders seçiniz mat121--ist--iktisat--olasılık1--ingilizce--bilgisayar--türkdili :  yada çıkış için enter ı tuşlayınız: "))  
        while dersSeçiniz=="iktisat" or dersSeçiniz=="mat121" or dersSeçiniz=="ist" or dersSeçiniz=="olasılık1" or dersSeçiniz=="ingilizce" or dersSeçiniz=="bilgisayar" or dersSeçiniz=="türkçe":
           
            dersSeçiniz=str(input("devam  etmek isterseniz dersi giriniz : mat121--ist--iktisat--olasılık1--ingilizce--bilgisayar--türkdili :  ya da 1 i tuşlayıp çıkabilirsiniz "))   
            if  dersSeçiniz=="mat121" :
                matvize1=int(input("matvize1: "))
                matvize2=int(input("matvize2: "))
                matfinal=int(input("matfinal: "))
                matort=int(((matvize1*3/10)+(matvize2*3/10)+(matfinal*4/10)))
                print("ortalamanız: ",matort)     ##ortalama hesaplatma
                i=matort                   

            elif dersSeçiniz=="ist":
            
                vize=int(input("vize notunuz: "))
                final=int(input("final notunuz: "))
                dönemödevinotunuz=int(input("dönem ödevi notunuz: "))
                istort=int((dönemödevinotunuz*2/10)+(vize*3/10)+(final*5/10))
                print("ortalamanız: ",istort)
                i=istort

            elif dersSeçiniz=="iktisat":
                iktisatvize=int(input(" vize notunuz : "))
                iktisatfinal=int(input("final notunuz: "))
                iktort=int((iktisatvize*4/10)+(iktisatfinal*6/10))
                print("ortalamanız: ",iktort)
                i=iktort

            elif dersSeçiniz=="olasılık1" :
                vize=int(input("vize notunuz: "))
                final=int(input("final notunuz: "))
                olasılıkort=int((vize+final)/2)
                print("ortalamanız: ",olasılıkort)
                i=olasılıkort

            elif dersSeçiniz=="ingilizce" :
                vize=40
                final=int(input("final notunuz: "))
                ingort=int((vize+final))
                print("ortalamanız: ",ingort)
                i=ingort

            elif dersSeçiniz=="türkdili":
                vize=int(input("vize notunuz: "))
                final=int(input("final notunuz: "))
                tdkort=int((vize*4/10)+(final*6/10))
                print("ortalamanız: ",tdkort)
                i=tdkort

            elif dersSeçiniz=="bilgisayar":
                vize=int(input("vize notunuz: "))
                final=int(input("final notunuz: "))
                pcort=int((vize*4/10)+(final*6/10))
                print("ortalamanız: ",pcort)
                i=pcort


            while   True:   ##hangi ortalamanın hangi harf notuna karşılık geldiği
                if i>=0 and i<=100:            
                        if  i>=55 and i<70:     

                            if i>=55 and i<60:
                                print("C3 ile gectiniz ")
                                break
                            elif i>=60 and i<65:
                                 print("C2 ile gectiniz ")
                                 break
                            elif i>=65 and i<70:
                                print("C1 ile gectiniz ")
                                break

                        elif i>=70 and i<85:     

                            if i>=70 and i<75:
                                print("B3 ile gectiniz ")
                                break
                            elif i>=75 and i<80:
                                print("B2 ile gectiniz ")
                                break
                            elif i>=80 and i<85:
                                print("B1 ile gectiniz ")
                                break
                             

                        elif i>=85 and i<=100:         

                            if i>=85 and i<90:
                                print("A3 ile gectiniz ")
                                break
                            elif i>=90 and i<95:
                                print("A2 ile gectiniz ")
                                break
                            elif i>=95 and i<=100:
                                print("A1 ile gectiniz ")
                                break

                        elif i>=50 and i<55:
                            print("D ile gectiniz ")
                            break
                        else:
                            print("kaldınız")
                            break

                else:      #ortalamanız 100 üzeri ise hata 
                        print("hatalı notlar girdiniz ve ortalamanız 0-100 aralıgında değil ,lüten tekrar giriniz ")  
                break
        else :
                print("çıkış yaptınız ")
    

    elif  dönemseçiniz=="bahar":
            dersSeçiniz=str(input("ders seçiniz beb650--ist--iktisat--olasılık2--ingilizce--mat--cebir--türkdili:  yada çıkış için enter ı tuşlayınız: "))  
            while dersSeçiniz=="iktisat" or dersSeçiniz=="mat" or dersSeçiniz=="ist" or dersSeçiniz=="olasılık2" or dersSeçiniz=="ingilizce" or dersSeçiniz=="beb650" or dersSeçiniz=="cebir" or dersSeçiniz=="türkdili":

                dersSeçiniz=str(input("devam  etmek isterseniz dersi giriniz : beb650--ist--iktisat--olasılık2--ingilizce--mat--cebir--türkdili:  ya da 1 i tuşlayıp çıkabilirsiniz "))   
                if  dersSeçiniz=="ist":
                    vize=int(input("vize notunuz: "))
                    final=int(input("final notunuz: "))
                    dönemödevinotunuz=int(input("dönem ödevi notunuz: "))
                    ort=int((dönemödevinotunuz*2/10)+(vize*3/10)+(final*5/10))
                    print("ortalamanız: ",ort)
                    i=ort

                elif dersSeçiniz=="olasılık2":
                    vize=int(input("vize notunuz: "))
                    final=int(input("final notunuz: "))
                    ort=int((vize+final)/2)
                    print("ortalamanız: ",ort)
                    i=ort

                elif dersSeçiniz=="cebir":
                    vize=int(input("vize notunuz: "))
                    final=int(input("final notunuz: "))
                    quiz1=int(input("1. quiz notunuz :"))
                    quiz2=int(input("2. quiz notunuz :"))
                    ort=int((quiz1*5/100)+(quiz2*5/100)+(vize*40/100)+(final*50/100))
                    print("ortalamanız: ",ort)
                    i=ort
                
                elif dersSeçiniz=="iktisat":
                    iktisatvize=int(input(" vize notunuz : "))
                    iktisatfinal=int(input("final notunuz: "))
                    iktort=int((iktisatvize*4/10)+(iktisatfinal*6/10))
                    print("ortalamanız: ",iktort)
                    i=iktort

                elif dersSeçiniz=="mat":
                    matvize1=int(input("matvize1: "))
                    matvize2=int(input("matvize2: "))
                    matfinal=int(input("matfinal: "))
                    matort=int(((matvize1*3/10)+(matvize2*3/10)+(matfinal*4/10)))
                    print("ortalamanız: ",matort)
                    i=matort

                elif dersSeçiniz=="beb650":
                    vize=40
                    final=int(input("final notunuz: "))
                    iktort=int(vize+(final*6/10))
                    print("ortalamanız: ",iktort)
                    i=iktort

                elif dersSeçiniz=="ing128" or dersSeçiniz=="ingilizce":
                    vize=40
                    final=int(input("final notunuz: "))
                    ort=int((vize+final))
                    print("ortalamanız: ",ort)
                    i=ort

                elif dersSeçiniz=="türkdili" or dersSeçiniz=="türkdili2":
                    vize=int(input("vize notunuz: "))
                    final=int(input("final notunuz: "))
                    ort=int((vize*4/10)+(final*6/10))
                    print("ortalamanız: ",ort)
                    i=ort

                while   True:   ##hangi ortalamanın hangi harf notuna karşılık geldiği
                    if i>=0 and i<=100:            
                            if  i>=55 and i<70:     

                                if i>=55 and i<60:
                                    print("C3 ile gectiniz ")
                                    break
                                elif i>=60 and i<65:
                                    print("C2 ile gectiniz ")
                                    break
                                elif i>=65 and i<70:
                                    print("C1 ile gectiniz ")
                                    break

                            elif i>=70 and i<85:     

                                if i>=70 and i<75:
                                    print("B3 ile gectiniz ")
                                    break
                                elif i>=75 and i<80:
                                    print("B2 ile gectiniz ")
                                    break
                                elif i>=80 and i<85:
                                    print("B1 ile gectiniz ")
                                    break
                             

                            elif i>=85 and i<=100:         

                                if i>=85 and i<90:
                                    print("A3 ile gectiniz ")
                                    break
                                elif i>=90 and i<95:
                                    print("A2 ile gectiniz ")
                                    break
                                elif i>=95 and i<=100:
                                    print("A1 ile gectiniz ")
                                    break

                            elif i>=50 and i<55:
                                print("D ile gectiniz ")
                                break
                            else:
                                print("kaldınız")
                                break

                    else:      #ortalamanız 100 üzeri ise hata 
                        print("hatalı notlar girdiniz ve ortalamanız 0-100 aralıgında değil ,lüten tekrar giriniz ")  
                    break
            else :
                print("olmayan bir dersi seçtiniz. çıkış yaptınız ")


    elif dönemseçiniz!="güz" or  dönemseçiniz!="bahar" :
        print("güz/bahar yazmalıydınız . çıkış yaptınız")

else:
    print("1/2/3/4 girmeliydiniz. çıkış yaptınız")
    

    


                
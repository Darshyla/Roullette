from random import randrange

print("____________________ LUCKY NUMBER ____________________")
print("Chwazi nimewo ki koresponn ak sa ou vle fè a")
print("1-Jwenn eksplikasyon sou jwèt la\n2-Komanse jwe")
chwa=input()
while int(chwa)<1 or int(chwa)>2:
    print("Ou antre yon move nonb. Antre 1 oubyen 2")
    chwa=input()
if int(chwa)==1:
    print("Odinatè a ap jenere yon nonb sekrè nan yon entèval epi ou ap eseye devine li. Wap gen 5 chans. Chak fwa ou devine nonb lan nap diw si li pi piti oubyen pi gran ke nonb sekrè a.\n\n")
    chwa=2
if int(chwa)==2:
    kontinye=True
    while kontinye==True:
        print("Chwazi nivo difikilte pati wap jwe a")
        print("1-Fasil: [0-100]")
        print("2-Mwayen: [0-300]")
        print("3-Difisil: [0-500]")
        chwa=input()
        
        while int(chwa)<1 or int(chwa)>3:
            print("Ou antre yon move nonb. Antre 1 ou 2 ou 3")
            chwa=input()
        
        if int(chwa)==1:
            maksimom=100
        if int(chwa)==2:
            maksimom=300
        if int(chwa)==3:
            maksimom=500

        nonb_sekre=randrange(0,maksimom)

        print("__________________________________________________________________________")
        print("Pou pwofesè a ka teste pwogram nan pi byen, nou afiche nonb sekrè a pou li")
        print("                         Nonb sekrè:", nonb_sekre,"                       ")
        print("__________________________________________________________________________")

        print("\n\nPati a komanse, devine nonb sekrè a\n\n")

        for i in range(1,6):
            print("Ou rete",6-i,"chans")
            nonb_devine=input()
            if int(nonb_devine)<int(nonb_sekre):
                print("Nonb sekrè a pi gran ke",nonb_devine)
            if int(nonb_devine)>int(nonb_sekre):
                print("Nonb sekrè a pi piti ke",nonb_devine)
            if i==5 and nonb_devine!=nonb_sekre:
                print("Dezole!!!!! Ou pèdi")
            if int(nonb_devine)==int(nonb_sekre):
                print("\nFelisitasyon!!!!!! Ou jwenn nonb sekrè a")
                break

        print("Nonb sekrè a se: ", nonb_sekre)
    
        print("\nSi ou anvi rejwe tape 1 sinon tape nenpot bagay")
        rejwe=input()
        if rejwe=="1":
            kontinye=True
        else:
            kontinye=False
            print("Mèsi paske ou te jwe ak nou. Ala pwochèn!!")

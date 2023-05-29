from pyDatalog import pyDatalog

pyDatalog.create_terms('X, log') 
pyDatalog.create_terms('rock, alt_rock, hard_rock, heavy_metal, doom_metal, hardcore_punk, punk_rock') 
pyDatalog.create_terms('screamo, acid_rock, math_rock, progressive_rock, psychedelic_rock, space_rock, shoegaze')
pyDatalog.create_terms('grunge, new_wave, hands_up, freakbeat, sigilkore, deep_internet, goregrind, grindcore')

#makin the data lists

gen = [
       rock, alt_rock, hard_rock, heavy_metal, doom_metal, 
       hardcore_punk, punk_rock, screamo, acid_rock, math_rock,
       progressive_rock, psychedelic_rock, space_rock, shoegaze, 
       grunge, new_wave, hands_up, freakbeat, sigilkore, deep_internet,
       goregrind, grindcore
       
       ]

with open('queen_db.txt') as queen:
    msc = queen.readlines()
msc = [x.rstrip('\n').replace(' ', '_').lower() for x in msc]


##### functions #####

def menu(l1, l2):

    gen_copy = l1.copy()
    msc_copy = l2.copy()

    print('\n::::: menu :::::', '\n[1] show artist list', '\n[2] show genre list', '\n[0] exit\n')
    menu_opt = int(input('>> '))

    match menu_opt:
        
        case 1:
            print("\n___artist list___")
            msc_set = (list(set(msc_copy)))
            msc_set.sort()
            msc_set.remove('|')
            for artist in msc_set:
                print(":: ", (artist).replace('_', ' ').title())
            msc_set = []
            menu(l1,l2) #loop
        
        case 2:
            print("\n___genre list___")
            gen_copy.sort()
            for genre in gen_copy:
                genre = str(genre).replace('_', ' ').title()
                print(':: ', genre)
            gen_copy = []
            menu(l1,l2) #loop
        
        case 0:
            ... #loop break

def queen_engine(l1, l2, artist, index):

    gen_copy = l1.copy()
    msc_copy = l2.copy()

    +log(index, artist) #submits
    
    for genre in gen_copy:
        for artist in msc_copy:
            if (artist=='|'):
                wall = (msc_copy.index('|')) + 1
                msc_copy = msc_copy[wall:]
                break
            else:
              genre(X) <= log(X, artist) #creating rules
        for som in genre(X):
            som = str(som).replace('(', '').replace(')','').replace(',','')
            if((som==str(index))==True):
                result = str(genre).replace('_', ' ').title()
                print("   *", result)
    gen_copy = []
    msc_copy = []


def queen_recs(l1, l2, genre_opt):

    gen_copy = l1.copy()
    msc_copy = l2.copy()

    for genero in gen_copy:
        for artist in msc_copy:
            if(str(genero)==genre_opt) & (artist!='|'):
                print("   *", (artist).replace('_', ' ').title())
            else:
                wall = (msc_copy.index('|')) + 1
                msc_copy = msc_copy[wall:]
                break
    gen_copy = []
    msc_copy = []


id_ = 1
def queens_playlist(i):

    ctrl = input("\n(=^‥^=)... ")
    if(ctrl=='#'): #loop break
        print('\nexiting...(シ. .)シ')
        ...
    else:
        while(ctrl=='m'):
            menu(gen, msc)
            print("\nready now?")
            ctrl = input("(Φ ω Φ)... ")

        match ctrl:
            
            case '1':
                art = input("\nenter artist: ").replace(' ', '_').lower()
                while(art=='m'): #initiating menu loop
                    menu(gen, msc)
                    print("\n(ᵔ◡ᵔ)")
                    art = input("enter artist: ").replace(' ', '_').lower()
                print('\n°˖✧ contemplated genres ✧˖°\n')
                queen_engine(gen, msc, art, i)
                i+=1

            case '2': 

                genre = input("\nenter genre: ").replace(' ', '_'.lower())
                while(genre=='m'): #initiating menu loop
                    menu(gen, msc)
                    print("\n(ᵔ◡ᵔ)")
                    genre = input("enter genre: ").replace(' ', '_').lower()
                print('\n°˖✧ contemplated artists ✧˖°\n')
                queen_recs(gen, msc, genre)
        
        queens_playlist(i) #loop



###################     homescreen     #######################

print("(„• ᴗ •„) welcome to queen's playlist", "\n\n(1) check genres of an artist", 
      "\n(2) check artists of a genre", "\n(#) exit queen's playlist", 
      "\n** press m to see the menu",'\n')

queens_playlist(id_)

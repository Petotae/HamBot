# Peter Savinelli

# Imports Hamilton class, and text to speech stuff
import Hamilton
from gtts import gTTS
from playsound import playsound
import os

# Creates a new Hamilton object
ham = Hamilton.Hamilton()


# Function that creates an MP3 File that contains a text to speech voice of "text", it then gets played then deleted
def talk(text):
    tts = gTTS(text)
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")


# Prints out Hamilton ASCII art
print("""                                                                                
                                     #%%(%&&                                    
                               @ /%%&#(#(  ,,.,..(##&@                          
                              &(.(%%,,,.#&.*/**      ,%#((&@                    
                          &.%(&&(#&((/#**  #**      . #/.%@&&@&*                
                         %( (  ,..../,. ,       %* ,(#* (*,,#(/&&@              
                    &.@&## . ,       ,. , *  . /..,..  ./, ,,.*../@/            
                   (&#%(  , (,. .   #/         ,%,            * .#(*#@          
                  &&,.   (../#(/*#*& . *       ..*/ ,    &&# .%%(.//,(          
                  .%.%.,./,..%//(%,.  (,.,. .((**/,*, %..  .**, /(&%&           
                  &&@./ ,* .# ,    *..(.*,,  ,.(/. . ,, *((/## (/*#%&@          
                 @&&.    .. (,..,,,, .. ,. **#/,/,,/.#/#***,#,,/%#&%&&          
                @@@&#&%&@@@///. (@&&*((&/*   . ,**,/((,/,,,((&&%&%#/#&          
               @& @(,&&@@./..  . (#%@@@@&*/*,,  *#%/(.(*,,/.#%##&#(((%          
                @&*%(&,#( ,. , , . ( .(,  .   *../, //%.#(%##&%/#, %&.&&        
                ,* &*.  *&   ,                 */ .# (*(. #*#,((,(  %*%@        
                       *    ..   ., (    , .  &&& &%.*(%#/%*&& & /  *#*/        
                   #*.%,       .    ,.  .. (*%* @&&#%%&&%&&&@%%.*%,,&&&         
                   @(%,@&#@&&&*/        * .//%  @.%%&%%&/,,#@/%@%&#&            
                   .*(,&( .     ,      ...#.*/,/*(,%#&@, ,((%#                  
                    #,/#(    . /*.      . /*,.,/ *,# &(,/&@(%%&                 
                    @(.#.**..,.,,        ,..%* @ ,/(%/,*&&%(/&#.                
                     &*(#...  .     /.  ,. .%*.,//&&(, %/&,&(&&#                
                     (& . .,.   , .*,* ...,#(*#&&/ (,#  #./@&@&@.               
                     %%, , #.    .(*//(,%/(@%@ . (/.(,#* @.@.&&...              
                   @&@(@&%&#,/*//%&%@@&@&%## .% ,./   @ @.@//@/@@@              
                 @&.@(&&&#.(@/&&@&%&%#&@& *# *      &.&&,@@& @*@*               
                &@%#(@(@(&#&&@%#%@&&%* .,.,,#.@  &*/@&(*&#@%&@&@.(@             
               @@&%(@&&*&*(/ @ * %#%& #%    *.@% %@@@%&,*(&#/%,& #/             
              /&%%@#%%&&%&&%(          (//%&&&./&@@@%&(%%&&%(&/@/%*&@           
              &%(&#&#% /  /, .  /##  &&&&&%/%&&@&&@&@&&#%#&(&@/&#((##&#%@       
               @%%@#  #*&%/%%&#  /%%@&(&((*(#%#%&#&%&&&#%&&/&#&*#/&(#&,(&&#@    
                 ./&    ( &@@&@%%&(&&,.##%&&#%@%#%&@@&/&@&#&@##&@.@*,%%#%.      
                    ,@&  #( &%#(@ &@//#@@@@&@&&@&&&&%(,&&@#&(&@.&.#&.@.         
                        @,* (#@%#@@@@/ @@&&&@@@&&@@*%#@&@,@#@.%,&@@             
                             @% @,@%@&/#..@*%&*@(%@&&@#,@@@@*@ """)

# Hamilton greets user, this is then printed and spoken with text to speech
greeting = ham.greet()
print(greeting)
talk(greeting)

# While loop makes up the rest of the program, it prompts the user, Hamilton responds, then text to speech is called
while True:
    prompt = input("\nInput: ")
    response = ham.genres(prompt)
    print("\nResponse: " + response)
    talk(response)

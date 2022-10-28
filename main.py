import songs
import random


def check_title(songs,prompt):
  valid = False
  while not valid:
    title = input(prompt)
    title = title.lower()
    if title == 'rules':
      rules()
    else:
      for i in range(len(songs)):
        if title == songs[i].title:
          valid = True
          return songs[i]

      print("Error - input not valid, type 'rules' for input rules\nPlease try again.")


def compare_album(input, correct_song):
  if input.album > correct_song.album:
    if (input.album - correct_song.album <= 1):
      return "⬇+"
    else:
      return "⬇"
      
  elif input.album < correct_song.album:
    if (correct_song.album - input.album <= 1):
      return "↑+"
    else:
      return "↑"
  else:
    return "✓"

def compare_pos(input, correct_song):
  if input.pos > correct_song.pos:
    if (input.pos - correct_song.pos <= 2):
      return "⬇+"
    else:
      return "⬇"
      
  elif input.pos < correct_song.pos:
    if (correct_song.pos - input.pos <= 2):
      return "↑+"
    else:
      return "↑"
  else:
    return "✓"
    

def compare_length(input, correct_song):
  if input.length > correct_song.length:
    if (input.length- correct_song.length <= 30):
      return "⬇+"
    else:
      return "⬇"
      
  elif input.length < correct_song.length:
    if (correct_song.length - input.length <= 30):
      return "↑+"
    else:
      return "↑"
  else:
    return "✓"

def compare_feat(input, correct_song):
  if input.feature == correct_song.feature:
    return " ✓"
  else:
    return " x"

def rules():
  print("GENERAL RULES:\n-You get 8 guesses to guess a mystery song off of all Kendrick studio albums besides the Black Panther album. (Albums: Section 80, GKMC, TPAB, Untitled Unmastered, DAMN., MMATBS\n--Album symbols: There are arrows hinting lower(⬇) and higher(↑) if there is a plus(+) next to the arrow, it means you are within 1 album.If you have the correct album, there will be a check(✓).\n--Track number symbols: There are arrows hinting lower(⬇) and higher(↑) if there is a plus(+) next to the arrow, it means you are within 2 tracks.If you have the correct track number, there will be a check(✓).\n--Track length symbols: There are arrows hinting lower(⬇) and higher(↑) if there is a plus(+) next to the arrow, it means you are within 30 seconds.If you have the track length, there will be a check(✓).\n--Features:There are only two symbols, check(✓), meaning you are ABSOLUTELY correct, and (x) meaning you are incorrect.(PARTIALLY CORRECT FEATURES WILL BE MARKED AS INCORRECT)")
  print("FORMATTING RULES:\n-Capitalization should not matter, but in case, type in all lowercase\n- Make sure you do not include any characters in your song, such as commas, periods, etc.\nFor example = 'M.A.A.D City' should be spelled 'Maad city'.\n-Any songs, such as 'sherane aka mr splinters daughter' have been shortened to sherane. This includes section 80 songs that have extra text in parantheses such as 'keishas song (her pain)' are just typed as keishas song, etc.\nText shaun if you have questions.")
  
  







def main():
  s1 = songs.SongAt("fuck your ethnicty", 1, 1, 224, "Colin Munroe")
  s2 = songs.SongAt("hol up", 1, 2, 173, "none")
  s3 = songs.SongAt("adhd", 1, 3, 215, "none")
  s4 = songs.SongAt("no make up", 1, 4, 235, "none")
  s5 = songs.SongAt("tammys song", 1, 5, 161, "none")
  s6 = songs.SongAt("chapter six", 1, 6, 161, "none")
  s7 = songs.SongAt("ronald reagan era", 1, 7, 216,   "none")
  s8 = songs.SongAt("poe mans dreams", 1, 8, 261, "GLC")
  s9 = songs.SongAt("the spiteful chant", 1, 9, 320, "ScHoolboy Q")
  s10 = songs.SongAt("chapter ten", 1, 10, 75, "none")
  s11 = songs.SongAt("keishas song", 1, 11, 227, "Ashtrobot")
  s12 = songs.SongAt("rigamortis", 1, 12, 168, "none")
  s13 = songs.SongAt("kush and corinthians", 1, 13, 304, "BJ the Chicago Kid")
  s14 = songs.SongAt("blow my high", 1, 14, 215, "none")
  s15 = songs.SongAt("absouls outro", 1, 15, 350, "Ab-Soul")
  s16 = songs.SongAt("hiiipower", 1, 16, 279, "none")


  s17 = songs.SongAt("sherane", 2, 1, 273, "none")
  s18 = songs.SongAt("bitch dont kill my vibe", 2, 2, 310, "none")
  s19 = songs.SongAt("backseat freestyle", 2, 3, 212, "none")
  s20 = songs.SongAt("the art of peer pressure", 2, 4, 324, "none")
  s21 = songs.SongAt("money trees", 2, 5, 386, "Jay Rock")
  s22 = songs.SongAt("poetic justice", 2, 6, 300, "Drake")
  s23 = songs.SongAt("good kid", 2, 7, 214, "none")
  s24 = songs.SongAt("maad city", 2, 8, 350, "MC Eiht")
  s25 = songs.SongAt("swimming pools", 2, 9, 313, "none")
  s26 = songs.SongAt("sing about me im dying of thirst", 2, 10, 723, "none")
  s27 = songs.SongAt("real", 2, 11, 443, "Anna Wise")
  s28 = songs.SongAt("compton", 2, 12, 248, "Dr. Dre")
  s29 = songs.SongAt("the recipe", 2, 13, 352, "Dr. Dre")
  s30 = songs.SongAt("black boy fly", 2, 14, 278, "none")
  s31 = songs.SongAt("now or never", 2, 15, 257, "Mary J. Blige")
  
  s32 = songs.SongAt("wesleys theory", 3, 1, 287, "George Clinton;Thundercat")
  s33 = songs.SongAt("for free", 3, 2, 130, "none")
  s34 = songs.SongAt("king kunta", 3, 3, 234, "none")
  s35 = songs.SongAt("institutionalized", 3, 4, 271, "Bilal;Anna Wise;Snoop Dog")
  s36 = songs.SongAt("these walls", 3, 5, 300, "Bilal;Anna Wise;Thundercat")
  s37 = songs.SongAt("u", 3, 6, 268, "none")
  s38 = songs.SongAt("alright", 3, 7, 219, "none")
  s39 = songs.SongAt("for sale", 3, 8, 291, "none")
  s40 = songs.SongAt("momma", 3, 9, 283, "none")
  s41 = songs.SongAt("hood politics", 3, 10, 292, "none")
  s42 = songs.SongAt("how much a dollar cost", 3, 11, 261, "James Fauntleroy;Ronald Isley")
  s43 = songs.SongAt("complexion", 3, 12, 263, "Rapsody")
  s44 = songs.SongAt("the blacker the berry", 3, 13, 328, "none")
  s45 = songs.SongAt("you aint gotta lie", 3, 14, 241, "none")
  s46 = songs.SongAt("i", 3, 15, 336, "none")
  s47 = songs.SongAt("mortal man", 3, 16, 727, "none")
  
  s48 = songs.SongAt("untitled 01", 4, 1, 247, "Bilal;Anna Wise")
  s49 = songs.SongAt("untitled 02", 4, 2, 258, "none")
  s50 = songs.SongAt("untitled 03", 4, 3, 154, "Bilal;Mani Strings")
  s51 = songs.SongAt("untitled 04", 4, 4, 110, "Rocket;SZA")
  s52 = songs.SongAt("untitled 05", 4, 5, 338, "Punch;Jay Rock;Bilal;Anna Wise")
  s53 = songs.SongAt("untitled 06", 4, 6, 208, "CeeLo Green")
  s54 = songs.SongAt("untitled 07", 4, 7, 496, "Egypt;SZA")
  s55 = songs.SongAt("untitled 08", 4, 8, 235, "Thundercat")
  
  s56 = songs.SongAt("blood", 5, 1, 118, "none")
  s57 = songs.SongAt("dna", 5, 1, 185, "none")
  s58 = songs.SongAt("yah", 5, 1, 160, "none")
  s59 = songs.SongAt("element", 5, 1, 208, "none")
  s60 = songs.SongAt("feel", 5, 1, 214, "none")
  s61 = songs.SongAt("loyalty", 5, 1, 227, "Rihanna")
  s62 = songs.SongAt("pride", 5, 1, 275, "none")
  s63 = songs.SongAt("humble", 5, 1, 177, "none")
  s64 = songs.SongAt("lust", 5, 1, 307, "none")
  s65 = songs.SongAt("love", 5, 1, 213, "Zacari")
  s66 = songs.SongAt("xxx", 5, 1, 254, "U2")
  s67 = songs.SongAt("fear", 5, 1, 460, "none")
  s68 = songs.SongAt("god", 5, 1, 248, "none")
  s69 = songs.SongAt("duckworth", 5, 1, 248, "none")
  
  s70 = songs.SongAt("united in grief", 6, 1, 255, "none")
  s71 = songs.SongAt("n95", 6, 2, 195, "none")
  s72 = songs.SongAt("worldwide steppers", 6, 3, 203, "none")
  s73 = songs.SongAt("die hard", 6, 4, 239, "Blxst;Amanda Reifer")
  s74 = songs.SongAt("father time", 6, 5, 222, "Sampha")
  s75 = songs.SongAt("rich interlude", 6, 6, 103, "Kodak Black")
  s76 = songs.SongAt("rich spirit", 6, 7, 202, "none")
  s77 = songs.SongAt("we cry together", 6, 8, 341, "Taylour Paige")
  s78 = songs.SongAt("purple hearts", 6, 9, 329, "Summer Walker;Ghostface Killah")
  s79 = songs.SongAt("count me out", 6, 10, 283, "none")
  s80 = songs.SongAt("crown", 6, 11, 264, "none")
  s81 = songs.SongAt("silent hill", 6, 12, 220, "Kodak Black")
  s82 = songs.SongAt("savior interlude", 6, 13, 152, "Baby Keem")
  s83 = songs.SongAt("savior", 6, 14, 224, "Baby Keem;Sam Dew")
  s84 = songs.SongAt("auntie diaries", 6, 15, 281, "none")
  s85 = songs.SongAt("mr morale", 6, 16, 210, "Tanna Leone")
  s86 = songs.SongAt("mother i sober", 6, 17, 406, "Beth Gibbons")
  s87 = songs.SongAt("mirror", 6, 18, 256, "none")

  songlist = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87]

  print("Welcome to Kdotle 1.0.")
  attempts = 0
  win_checker = False
  s = f"|{'TITLE':^30}|{'ALBUM':^9}|{'TRACK NO.':^9}|{'TRACK LENGTH':^14}|{'FEATURES':^20}|\n"
  winning_word = songlist[random.randint(0,86)]

  while attempts < 8 and win_checker == False:
    attempts += 1
    guess = check_title(songlist, f"({attempts}/8)Enter Kdot Song: ")

    if guess.album == 1:
      guess_album = "SC80"
    elif guess.album == 2:
      guess_album = "GKMC"
    elif guess.album == 3:
      guess_album = "TPAB"
    elif guess.album == 4:
      guess_album = "UNTI"
    elif guess.album == 5:
      guess_album = "DAMN"
    else:
      guess_album = "MMBS"

    if guess.length%60<10:
      guess_seconds = f"0{guess.length%60}"
      
    else:
      guess_seconds = str(guess.length%60)
      
    guess_length = f"{guess.length//60}:{guess_seconds}"
    
    s += f"{guess.title:^32}{guess_album+compare_album(guess,winning_word):^9}{str(guess.pos)+compare_pos(guess,winning_word):^11}{guess_length+  compare_length(guess,winning_word):^16}{guess.feature + compare_feat(guess,winning_word):^22}\n"

    print(s)

    if guess.title == winning_word.title:
      print(f"Congratulations, you got the song in {attempts} trys!")
      win_checker = True

  if win_checker == False: 
    print(f"The song was '{winning_word.title}'. Better luck next time!")



  





main()
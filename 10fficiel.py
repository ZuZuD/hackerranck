def Reducelist(tab,total1,total2):
   for i in range((len(tab)/2)):
     if (total1 == total2):
       return True
     if (total1<total2):
       total1+=tab[len(tab)/2+i]
       total2-=tab[len(tab)/2+i+1]
     else:
       total1-=tab[len(tab)/2-i-1]
       total2+=tab[len(tab)/2-i]
     print 'total1 :'+ str(total1) +' total2 :'+ str(total2)
   return False

if __name__ == '__main__':
  array1= [48,1,2,1,15,20,10]
  array2=[3,12,18,1,1,1,1,1,37]
  array3=[377, 159, 26, 86, 141, 56, 191, 51, 293, 105, 24, 425, 419, 159, 311, 112, 408, 123, 141, 234, 79, 432, 317, 485, 200, 56, 64, 374, 174, 339, 100, 9, 384, 275, 22, 35, 144, 267, 179, 160, 207, 224, 18, 221, 398, 466, 196, 463, 145, 52, 479, 337, 462, 308, 88, 139, 130, 76, 58, 413, 305, 56, 432, 260, 273, 329, 134, 350, 159, 28, 333, 345, 482, 373, 326, 64, 310, 421, 416, 446, 426, 456, 119, 332, 214, 399, 117, 331, 154, 147, 48, 480, 29, 72, 426, 167, 399, 275, 264, 9, 380, 321, 88, 433, 127, 402, 375, 363, 271, 378, 64, 76, 213, 63, 207, 391, 440, 306, 87, 275, 203, 429, 372, 386, 191, 463, 345, 64, 275, 456, 243, 495, 462, 61, 460, 500, 232, 418, 194, 220, 454, 103, 9, 145, 205, 162, 65, 492, 175, 415, 257, 470, 222, 15, 413, 140, 346, 354, 481, 177, 384, 457, 464, 80, 357, 120, 358, 19, 327, 429, 86, 373, 309, 447, 360, 229, 34, 368, 464, 41, 287, 224, 426, 440, 261, 8, 391, 453, 374, 52, 63, 333, 365, 496, 281, 60, 358, 375, 397, 389, 188, 119, 491, 310, 190, 455, 352, 173, 369, 5, 364, 49, 272, 292, 495, 54, 70, 100, 223, 400, 404, 293, 485, 404, 457, 379, 384, 16, 304, 73, 105, 318, 369, 13, 285, 417, 240, 161, 166, 268, 373, 434, 146, 165, 490, 160, 270, 294, 196, 163, 372, 152, 31, 349, 345, 283, 85, 317, 84, 427, 319, 370, 354, 122, 56, 90, 72, 432, 404, 399, 464, 378, 258, 350, 124, 147, 98, 446, 2, 418, 316, 50, 46, 42, 27, 152, 343, 461, 415, 31, 222, 153, 475, 362, 293, 434, 208, 94, 93, 310, 440, 500, 428, 199, 204, 93, 456, 289, 139, 224, 495, 34, 208, 191, 409, 88, 296, 383, 153, 122, 482, 403, 108, 315, 77, 189, 432, 305, 393, 410, 331, 379, 154, 221, 105, 112, 136, 187, 194, 50, 225, 125, 213, 160, 422, 81, 438, 45, 435, 397, 77, 426, 234, 151, 160, 115, 296, 308, 313, 391, 272, 416, 326, 212, 421, 444, 36, 448, 316, 88, 76, 342, 421, 62, 177, 38, 313, 153, 376, 201, 146, 62, 258, 266, 303, 50, 421, 187, 48, 18, 340, 136, 107, 74, 226, 323, 246, 155, 199, 483, 459, 169, 472, 314, 9, 41, 462, 387, 74, 180, 119, 404, 23, 423, 412, 268, 458, 297, 424, 123, 497, 32, 27, 361, 272, 467, 188, 262, 355, 141, 460, 294, 346, 257, 493, 461, 447, 408, 472, 271, 71, 311, 239, 387, 434, 66, 164, 466, 434, 434, 207, 413, 324, 232, 472, 217, 295, 400, 251, 5, 378, 470, 342, 195, 258, 440, 499, 199, 314, 127, 11, 451, 258, 389, 213, 489, 273, 289, 20, 4, 331, 339, 52, 319, 416, 444, 130, 328, 446, 152, 495, 54, 446, 347, 18, 280, 116, 31, 399, 108]
  array=[array1,array2,array3]

  for tab in array:
    if len(tab) == 1:
      print 'YES'
    total1 = sum(tab[:len(tab)/2])
    total2 = sum(tab[len(tab)/2+1:])
    if (Reducelist(tab,total1,total2)):
      print 'YES'
    else:
      print 'NO'
 

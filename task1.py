bad = r''' *    *    .  *    // *            .  *
     *  .  ..  *  //.     *      *        *    .
..    *  ___o |==//     .      *   *
        /\  \/  //|\   *  .  ..   *       *
ejm96  / /        | \
       ` `        '  '
       '''

good = r'''@  *  .  . *       *    .        .        .   *    ..
 @. /\ *     ###     .      .        .            *
 @ /  \  *  #####   .     *      *        *    .
 ]/ [] \  ######### *    .  *       .  //    .  *   .
 / [][] \###\#|#/###   ..    *     .  //  *  .  ..  *
 |  __  | ###\|/###  *    *  ___o |==// .      *   *
 |  |!  |  # }|{  #         /\  \/  //|\
 |  ||  |    }|{    ejm97  / /        | \
                           ` `        '  '
'''

torch_lit = True
outcome = "Flicker: Success, it's lit! I can see everything!"
if torch_lit:
    print(good)

else:
    outcome = "Doom: Noooooo! I'm doomed! Only the stars to light my way!"
    print(bad)
print(outcome)
from jam import run_jam_code

#Example: check the sign of an inputted number
function check_sign(n) {
    if n > 0 {
        print "positive"
    } else {
        if n < 0 {
            print "negative"
        } else {
            print "zero"
        }
    }
}

check_sign(5)
check_sign(-3)
check_sign(0)
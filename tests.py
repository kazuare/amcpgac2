sys.path.append(os.path.abspath("FlaskWebProject"))
from views import isPalindrome

if isPalindrome("23"):
    sys.exit(99)

sys.exit(9)

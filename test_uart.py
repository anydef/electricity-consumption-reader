import smllib

messages = [
    b'\xff\xffrb\x01e\x11A\xe3\xd4zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TF\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xf1\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01_\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\x9c\xd2\x00v\t\x80\x00\x00\x00\x02iznb\x00b\x00rc\x02\x01q\x01c\x18\xcf\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x9a\x1e\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02izob\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffj\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xc8\xc8\x00v\t\x80\x00\x00\x00\x02izpb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xd7zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TH\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xf3\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01Y\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c*\x8a\x00v\t\x80\x00\x00\x00\x02izqb\x00b\x00rc\x02\x01q\x01c\x11\xa2\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x8f\x1c\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02izrb\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffl\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xaa\xe7\x00v\t\x80\x00\x00\x00\x02izsb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xd9zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TJ\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xf5\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01W\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c]\n'
    ,b'\x00v\t\x80\x00\x00\x00\x02iztb\x00b\x00rc\x02\x01q\x01c\xd5\xa9\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x17$\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02izub\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffm\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xa4C\x00v\t\x80\x00\x00\x00\x02izvb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xdbzw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TL\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xf7\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01K\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\x8f\x92\x00v\t\x80\x00\x00\x00\x02izwb\x00b\x00rc\x02\x01q\x01cfW\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xf8\x7f\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02izxb\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffo\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\x12\x9a\x00v\t\x80\x00\x00\x00\x02izyb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xddzw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TN\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xf9\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01Y\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01cBD\x00v\t\x80\x00\x00\x00\x02izzb\x00b\x00rc\x02\x01q\x01c\x08\xe0\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xe4\xc6\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz{b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffq\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\x12\xeb\x00v\t\x80\x00\x00\x00\x02iz|b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xdfzw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TP\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xfb\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01Q\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c~\xe6\x00v\t\x80\x00\x00\x00\x02iz}b\x00b\x00rc\x02\x01q\x01c\xee@\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x96\xa3\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz~b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffs\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xd0i\x00v\t\x80\x00\x00\x00\x02iz\x7fb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xe1zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TR\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xfd\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01N\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\xd3\xec\x00v\t\x80\x00\x00\x00\x02iz\x80b\x00b\x00rc\x02\x01q\x01cQ;\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xf3K\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x81b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffu\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c9a\x00v\t\x80\x00\x00\x00\x02iz\x82b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xe3zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TT\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd5\xff\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01R\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01ctS\x00v\t\x80\x00\x00\x00\x02iz\x83b\x00b\x00rc\x02\x01q\x01c\xe2\xc5\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x0f\xe7\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x84b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffw\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xfb\xe3\x00v\t\x80\x00\x00\x00\x02iz\x85b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xe5zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TV\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\x01\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01V\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\xa6K\x00v\t\x80\x00\x00\x00\x02iz\x86b\x00b\x00rc\x02\x01q\x01c&\xce\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xcb[\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x87b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xffy\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\x1a\x9a\x00v\t\x80\x00\x00\x00\x02iz\x88b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xe7zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TX\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\x03\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01]\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\xf9\xba\x00v\t\x80\x00\x00\x00\x02iz\x89b\x00b\x00rc\x02\x01q\x01cj\xd2\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xcf\x14\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x8ab\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xff{\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xacC\x00v\t\x80\x00\x00\x00\x02iz\x8bb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xeazw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1TZ\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\x05\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01Y\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\x0e\xf8\x00v\t\x80\x00\x00\x00\x02iz\x8cb\x00b\x00rc\x02\x01q\x01c\xae\xd9\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02o\x95\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x8db\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xff}\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\x8f\x97\x00v\t\x80\x00\x00\x00\x02iz\x8eb\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b"\xff\xffrb\x01e\x11A\xe3\xeczw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1T\\\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\x07\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01R\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\x9e\xda\x00v\t\x80\x00\x00\x00\x02iz\x8fb\x00b\x00rc\x02\x01q\x01c\x1d'\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xe1\x03\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x90b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xff\x7f\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\xd1\xf8\x00v\t\x80\x00\x00\x00\x02iz\x91b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n"
    ,b'\xff\xffrb\x01e\x11A\xe3\xeezw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1T^\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\t\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01Y\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01cF\xca\x00v\t\x80\x00\x00\x00\x02iz\x92b\x00b\x00rc\x02\x01q\x01c6\xe1\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\xb1\xcf\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x93b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xff\x81\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c\x9f\xfc\x00v\t\x80\x00\x00\x00\x02iz\x94b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
    ,b'\xff\xffrb\x01e\x11A\xe3\xf0zw\x07\x81\x81\xc7\x82\x03\xff\x01\x01\x01\x01\x04DZG\x01w\x07\x01\x00\x00\x00\t\xff\x01\x01\x01\x01\x0b\t\x01DZG\x00\x01_)\x88\x01w\x07\x01\x00\x01\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb1T`\x01w\x07\x01\x00\x01\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x0f\xb0\xd6\x0b\x01w\x07\x01\x00\x01\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00>\x16\x01w\x07\x01\x00\x02\x08\x00\xffe\x00\x01\x01\x82\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00\xd8\x81\x01w\x07\x01\x00\x02\x08\x01\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00uU\x01w\x07\x01\x00\x02\x08\x02\xff\x01\x01b\x1eR\xffY\x00\x00\x00\x00\x00\x00#\xbf\x01w\x07\x01\x00\x0f\x07\x00\xff\x01\x01b\x1bR\x00e\x00\x00\x01T\x01w\x07\x81\x81\xc7\x82\x05\xff\x01\x01\x01\x01\x83\x02\xe6g\xd7\x96\xca\xe0]T\xf7\x84\xe5\xd2q\x15\xbe0\xb4`7\xb7n\x02tB\xb3\xf9\xb5\x93y\xbe\xee\x0f901\xd6\xb6L|\x83Z\xd4T#\x03[\x9ew\x01\x01\x01c\x96\x05\x00v\t\x80\x00\x00\x00\x02iz\x95b\x00b\x00rc\x02\x01q\x01c\xd0A\x00\x00\x00\x1b\x1b\x1b\x1b\x1a\x02\x06\\\x1b\x1b\x1b\x1b\x01\x01\x01\x01v\t\x80\x00\x00\x00\x02iz\x96b\x00b\x00rc\x01\x01v\x01\x0b0023013768\x0b\xff\xff\xff\xff\xff\xff\x83\xff\xff\xff\x0b\t\x01DZG\x00\x01_)\x88\x01\x01c]~\x00v\t\x80\x00\x00\x00\x02iz\x97b\x00b\x00rc\x07\x01w\x0b0023013768\x0b\t\x01DZG\x00\x01_)\x88\x07\x01\x00b\n'
]

OBIS_NAMES = {
    '0100000009ff': 'Geräteeinzelidentifikation',
    '0100010800ff': 'Zählerstand Total',
    '0100010801ff': 'Zählerstand Tarif 1',
    '0100010802ff': 'Zählerstand Tarif 2',
    '0100011100ff': 'Total-Zählerstand',
    '0100020800ff': 'Wirkenergie Total',
    '0100100700ff': 'aktuelle Wirkleistung',
    '0100170700ff': 'Momentanblindleistung L1',
    '01001f0700ff': 'Strom L1',
    '0100200700ff': 'Spannung L1',
    '0100240700ff': 'Wirkleistung L1',
    '01002b0700ff': 'Momentanblindleistung L2',
    '0100330700ff': 'Strom L2',
    '0100340700ff': 'Spannung L2',
    '0100380700ff': 'Wirkleistung L2',
    '01003f0700ff': 'Momentanblindleistung L3',
    '0100470700ff': 'Strom L3',
    '0100480700ff': 'Spannung L3',
    '01004c0700ff': 'Wirkleistung L3',
    '0100510701ff': 'Phasenabweichung Spannungen L1/L2',
    '0100510702ff': 'Phasenabweichung Spannungen L1/L3',
    '0100510704ff': 'Phasenabweichung Strom/Spannung L1',
    '010051070fff': 'Phasenabweichung Strom/Spannung L2',
    '010051071aff': 'Phasenabweichung Strom/Spannung L3',
    '010060320002': 'Aktuelle Chiptemperatur',
    '010060320003': 'Minimale Chiptemperatur',
    '010060320004': 'Maximale Chiptemperatur',
    '010060320005': 'Gemittelte Chiptemperatur',
    '010060320303': 'Spannungsminimum',
    '010060320304': 'Spannungsmaximum',
    '01000e0700ff': 'Netz Frequenz',
    '8181c78203ff': 'Hersteller-Identifikation',
    '8181c78205ff': 'Öffentlicher Schlüssel',
}


from smllib import SmlStreamReader

stream = SmlStreamReader()
for m in messages:
    stream.add(m)


sml_frame = stream.get_frame()
if sml_frame is None:
    print('Bytes missing')

# Shortcut to extract all values without parsing the whole frame
obis_values = sml_frame.get_obis()

# return all values but slower
parsed_msgs = sml_frame.parse_frame()
for msg in parsed_msgs:
    # prints a nice overview over the received values
    print(msg.format_msg())

# The obis attribute of the SmlListEntry carries different obis representations as attributes
list_entry = obis_values[0]
print(list_entry.obis)            # 0100010800ff
print(list_entry.obis.obis_code)  # 1-0:1.8.0*255
print(list_entry.obis.obis_short) # 1.8.0
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * The <code>AccessEntry</code> class represents entries of Apache access.log files.
 * This is a primitive implementation of what is expected.
 * Thus, this is not for real life usage, only for training purpose.
 *
 * @version 1.0
 * @author yunes
 */
public class AccessEntry {
    private String address;
    private ZonedDateTime date;
    private String request;
    private String url;
    private String proto;
    private int code = -1;
    private int length = -1;
    private String referer;
    private UserAgent userAgent;
    private boolean state = true;
    private String text;
    private final String regex = "^(\\S+) (\\S+) (\\S+) " +
            "\\[([\\w:/]+\\s[+\\-]\\d{4})\\] \"(\\S+)" +
            " (\\S+)\\s*(\\S+)?\\s*\" (\\d{3}) (\\S+) \"(\\S+)\" \"([^\"]*)\" \"(.*)\"";
    private final Pattern pattern = Pattern.compile(regex);

    /**
     * Constructs a new <code>AccessEntry</code> from a given <code>String</code>.
     * Strings must roughly be in Apache custom log format, <em>i.e.:</em><br>
     * <pre>109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"</pre>
     * If the string can't be parsed, the object is in incorrect state and the string is stored in the text property.
     *
     * @param line the string to be parsed.
     */
    public AccessEntry(String line) {
        final Matcher matcher = pattern.matcher(line);
        if (matcher.find()) {
            address = matcher.group(1);
            String d = matcher.group(4);
            DateTimeFormatter format = DateTimeFormatter.ofPattern("dd/MMM/uuuu:HH:mm:ss Z", Locale.ENGLISH);
            date = ZonedDateTime.parse(d,format);
            request = matcher.group(5);
            url = matcher.group(6);
            proto = matcher.group(7);
            try {
                code = Integer.parseInt(matcher.group(8));
            } catch(NumberFormatException e) {}
            try {
                length = Integer.parseInt(matcher.group(9));
            } catch(NumberFormatException e) {}
            referer = matcher.group(10);
            userAgent = new UserAgent(matcher.group(11));
        } else {
            state = false;
            text = line;
        }
    }
    public String getProto() {
        return proto;
    }
    public int getCode() {
        return code;
    }
    public String getRequest() {
        return request;
    }
    public String getURL() {
        return url;
    }
    public boolean isCorrect() {
        return state;
    }
    public UserAgent getUserAgent() {
        return userAgent;
    }
    public ZonedDateTime getDate() {
        return date;
    }
    public int getLength() {
        return length;
    }
    public String getText() {
        return text;
    }
    public String toString() {
        if (state) {
            return "IP=" + address
                    + ", Date=" + date
                    + ", Request=" + request
                    + ", URL=" + url
                    + ", Proto=" + proto
                    + ", Code=" + code
                    + ", Length=" + length
                    + ", UserAgent" + userAgent
                    ;
        }
        return "Bad ("+text+")";
    }
}
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * This <code>UserAgent</code> class roughly represents userparsed user-agent strings.
 *
 * @author yunes
 * @version 1.0
 */
public class UserAgent {
    private String compatibility = "unparsed";
    private String platform = "unparsed";
    private final String compatibilityRegex = "^(\\p{Alpha}*)/\\S+";
    private final Pattern compatibilityPattern = Pattern.compile(compatibilityRegex);
    private final String platformRegex = "^\\p{Alpha}*/\\S+ \\((\\p{Alpha}+)[^\\)]*\\)";
    private final Pattern platformPattern = Pattern.compile(platformRegex);
    /**
     * This constructs an object that represents a parsed user-agent string.
     * Beware that this is a very very poor version of it, intented for training purpose only.
     * @param text the text to be parsed
     */
    public UserAgent(String text) {
        final Matcher compatibilityMatcher = compatibilityPattern.matcher(text);
        if (compatibilityMatcher.find()) {
            compatibility = compatibilityMatcher.group(1);
        } else {
            compatibility = "unknown";
        }
        final Matcher platformMatcher = platformPattern.matcher(text);
        if (platformMatcher.find()) {
            platform = platformMatcher.group(1);
        } else {
            platform = "unknown";
        }
    }
    public String getCompatibility() {
        return compatibility;
    }
    public String toString() {
        return "Platform="+platform
                +", Compatibility="+compatibility
                ;
    }
}
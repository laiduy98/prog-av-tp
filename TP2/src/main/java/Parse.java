import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.List;

public class Parse {
    public static void main(String[] args) throws IOException {

        List<String> list = Files.readAllLines(new File(args[0]).toPath(), Charset.defaultCharset());

        list.stream().map(line -> new AccessEntry(line)).forEach(System.out::println);

    }
}

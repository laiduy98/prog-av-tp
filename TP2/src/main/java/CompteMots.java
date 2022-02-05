import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class CompteMots {
    public static void main(String[] args) throws IOException {
//        parse in args[0] = pg20372.txt

//        File file = new File(args[0]);

        long wordsCount = Files.lines(Paths.get(args[0]))
                .flatMap(str-> Stream.of(str.split("[\n\\s+]")))
                .filter(s->s.length()>0).count();
        System.out.println(wordsCount);

    }
}

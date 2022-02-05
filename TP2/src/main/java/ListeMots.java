import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.Map;
import java.util.stream.Stream;

public class ListeMots {
    public static void main(String[] args) throws IOException {
//        parse in args[0] = pg20372.txt
        System.out.println("Hello");
//        File file = new File(args[0]);
        Map<String, Long> wordCountPair = Files.lines(Paths.get(args[0]))
                .flatMap(line -> Arrays.stream(line.trim().split("[\n\\s+]")))
                .map(word -> word.replaceAll("[^a-zA-Z]", "").toLowerCase().trim())
                .filter(word -> !word.isEmpty())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

//        System.out.println(wordCountPair);
        Stream.of(wordCountPair.keySet().toString()).forEach(System.out::println);
    }
}

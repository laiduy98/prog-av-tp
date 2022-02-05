import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Code {
    public static void main(String[] args) throws IOException {
//        parse in args[0] = access.log

        List<String> list = Files.readAllLines(new File(args[0]).toPath(), Charset.defaultCharset());
//        2.
//        Print all code of HTTP
        list.stream().map(line -> new AccessEntry(line)).map(code -> code.getCode()).forEach(System.out::println);
        System.out.println("\n---------------");
//        3.
//        Count number of HTTP code
        Map<Integer, Long> codeCountPair = list.stream()
                .map(line -> new AccessEntry(line))
                .map(code -> code.getCode())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));


        Stream.of(codeCountPair.keySet().toString()).forEach(System.out::print);
        System.out.println("  ");
        Stream.of(codeCountPair.values().toString()).forEach(System.out::println);
    }
}

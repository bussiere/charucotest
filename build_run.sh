#!/bin/bash
clear
echo "" > errors.txt
echo "1"
cp gradle_linux.properties gradle.properties
#rm build/libs/vampire_java-all-0.1.0.jar 2> /dev/null
echo "2"
#gradle build --stacktrace --warning-mode all > errors.txt 2>&1  && gradle run --warning-mode all>> errors.txt 2>&1 
gradle build --stacktrace --warning-mode all  && gradle run --warning-mode all
cat errors.txt
echo "3"
echo "creation jar" && gradle fatJar && echo "lancement jar" && java -jar build/libs/charucotest-all-0.1.0.jar  && cat errors.txt
#gradle build --stacktrace >> errors.txt 2>&1  && gradle run >> errors.txt 2>&1
gradle clean test

FROM openjdk:8

#mention the jar file path
COPY target/*.jar .  

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "*.jar"]
# How to Create a new Spring Boot Project

#### __NOTE:__ For this example we will use INTELLIJ IDEA but the steps to follow are simillar in others IDE

## USING SPRING BOOT INITIALIZER

We can use the Initializer tool available in any browser. Search Spring Boot Initializer and complete all requirements according to the configuration that we need.
![Logo Spring Boot](https://miro.medium.com/v2/resize:fit:1024/1*6xBxS9aeMgflfHGjJ3VfaA.png)

This is the URL of the official page [Spring Boot Initializer](https://start.spring.io/)

If we can to use this resource, we must download the generated project and we must import it as a MAVEN project in our IDE.

## USING THE IDE TO GENERATE THE PROJECT

Another way to generate a Spring Boot Project is using the IDE with the tools integrated.

1. Create a New Project.
2. Select Spring Boot with Java and Maven.
3. Fill the fields required

For this example we use the next configuration:

```text
Group: mx.com.gm          Name: HolaMundoSpring
Artifact: HolaSpring      Description: Hola Mundo 
Packagin: Jar             Package: mx.com.gm
```

The we use the next dependencies:
__Spring Boot DevTools, Lombok, Spring Boot Web and Thymeleaf__.

__NOTE:__ It's a good practice to use a path near to the C disk to avoid problems. For this example we use the path "C:\Cursos\SpringUdemy\"

If at this point the project shows an error, we must to make Clean & Build project to download the missing dependencies.

Now we can run the project. If the default port is not available we can change the port in the  application.properties file (\src\main\resources\application.properties). This step is optional.

```java
spring.application.name=HolaMundoSpring

# Change port
server.port=8081
```

### Running App
Intellij IDEA
![Run first app](/SpringBoot/img/RunFirstApp.png)

Local Host, port 8081
At this moment we should see and error, but it is correct because is the initial configuration.
![Local Host First App Error](/SpringBoot/img/FirstAppLocalHostError.png)
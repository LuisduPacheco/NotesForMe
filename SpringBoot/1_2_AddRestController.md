# ADD REST CONTROLLER

The Spring Framework is a class container, to recognize other classes they must be in the same package as the class annotated with @SpringBootApplication, for this example the main package is mx.com.gm, we can also use a subpackage like mx.com.gm.view.

![Main Anntoation](/SpringBoot/img/1_2_MainAnnotation.png)

## HOW TO ADD A REST CONTROLLER

Create a new class (can be any name), ControladorInicio.java in the package mx.com.gm, this class must have the @RestController annotation.

Create a public method that returns a String, add the @GetMapping("/") annotation to show the String in the browser accesing the localhost with port used (8081 for this example).
![Rest Controller](/SpringBoot/img/1_2_RestController.png)
![Local Host](/SpringBoot/img/1_2_DeployLocalHost.png)

The application automatically deploys the information as we can see in console due at the dependencies added when the project was created. In specific the Spring Boot Dev Tools. 

![Rest Controller](/SpringBoot/img/1_2_DeployConsole.png)

The format on console is due to application.properties, we can modify the format show info this is optional. 

```java
spring.application.name=HolaMundoSpring
# Change the port
server.port=8081

# Extra configuration to show logging format
logging.pattern.dateformat=hh:mm
```
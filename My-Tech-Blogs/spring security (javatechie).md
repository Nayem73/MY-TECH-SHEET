# @RequestBody and @ResponseBody

- when we use @RequestBody, it deserializes the json so that we can map the information that was present in the json into an object.

- when we use @ResponseBody above the above the @GetMapping or @PostMapping method, The `@ResponseBody` / above the class @RestController (not @Controller) annotation tells a controller that the object returned is automatically serialized into JSON and passed back into the HttpResponse object.

# PasswordEncoder

- we used bcrypt as PasswordEncoder:

```java
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
```

# SecurityConfig

- before, we had something called the WebSecurityConfigurerAdapter, It provided us 3 overloaded methods and we could perform authentication and authorization tasks easily. but in newer version of spring, WebSecurityConfigurerAdapter is depricated.

- So now, we need to create a @Bean of UserDetailsService for authentication related stuff.

- And, for Authorization related stuff, we have SecurityFilterChain, we also expose it as a @Bean. with this, we can configure which role can access which endpoints. for this, we can apply @PreAuthorize to specific endpoints. We also need to specify @EnableMethodSecurity in the SecurityConfig class for it. @PreAuthorize to specific methods is called method level authorization.

- Now, to store the userInfo, we create a userInfo class.

- Now, inside the UserDetailsService, we create our own custom UserDetailsService (we called it UserInfoUserDetailsService) that will interact with the database to fetch userinfo and return it.
  
  - our custom class UserInfoUserDetailsService implements the interface UserDetailsService and we will need to override the method loadUserByUsername(String username) from the parent interface UserDetailsService
  
  - Here, if we observe, the parent interface UserDetailsService gave us a method loadUserByUsername(String username) which has a return type UserDetails
  
  - Now, how do I create/get this UserDetails object (how can I convert the current userInfo to this UserDetails type so that I can return it)
  
  - so, let's find the userInfo from repository. For this, we need to inject userInfoRepository.
  
  - then I find the userInfo entity from repository and convert it to userDetails object like this:

```java
@Component
public class UserInfoUserDetailsService implements UserDetailsService {
    @Autowired
    private UserInfoRepository userInfoRepository;

    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // Retrieve UserInfo from the repository
        Optional<UserInfo> userInfo = userInfoRepository.findByUserName(username);

        if (userInfo.isPresent()) {
            // Create a new UserDetails object using the retrieved UserInfo
            UserInfoUserDetails userDetails = new UserInfoUserDetails(userInfo.get());
            return userDetails;
        } else {
            throw new UsernameNotFoundException("User not found: " + username);
        }
    }

}

        
```

- Now, to convert the userInfo to userDetails, we need to create another class (we called it UserInfoUserDetails). so we did UserInfoUserDetails implements UserDetails. Then we override all the methods that is available in the parent interface UserDetails.

- Now, we just need to define the fields that we have in our UserInfo entity, so that it gets converted to the UserDetails object. then simply with a constructor, we just populate these instance fields:

```java
public class UserInfoUserDetails implements UserDetails {
    private String userName;
    private String password;
    private List<GrantedAuthority> grantedAuthorityList;

    public UserInfoUserDetails(UserInfo userInfo) {
        this.userName = userInfo.getUserName();
        this.password = userInfo.getPassword();
        this.grantedAuthorityList = new ArrayList<>();

        String[] roles = userInfo.getRole().split(",");
        for (String role : roles) {
            grantedAuthorityList.add(new SimpleGrantedAuthority(role));
        }
    }
}
```

- So Now, I've given my custom UserDetailsService to the SecurityConfig

- --------

- Now, creating users according to their role, from the UserInfoController, we try to log in.

- But we will get an error: No AuthenticationProvideer found for org.springframework.security.authentication.UsernamePasswordAuthenticationToken

- Because, We have defined the UserDetailsService, who interacts with the Database, and validates the user. But we also need one AuthenticationProvider. Only the AuthenticationProvider will talk to the UserDetailsService. So, we need an instance of AuthenticationProvider in our SecurityConfig class.
  
  - So, we create a Bean of AuthenticationProvider. and inside the method, we will need an instance of DAOAuthenticationProvider
  
  - the information we need to give to the AuthenticationProvider: UserDetailsService and PasswordEncoder
  
  - If we pass these two information, then the AuthenticationProvider will interact/talk to the UserDetailsService and generate the UserDetailsService object and will set that as the AuthenticationProvider object.

```java
    @Bean
    public AuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider authenticationProvider = new DaoAuthenticationProvider();
        authenticationProvider.setUserDetailsService(userDetailsService());
        authenticationProvider.setPasswordEncoder(passwordEncoder());
        return authenticationProvider;
    }
```

# JWT Token

- The disadvantage of above approach is kind of nothing but for each and every endpoint, we will need to provide our username and password. for example product with page 1, page 2 << each of them would require putting in username, password.
- so, if we could store the log in session for a particular time, once the user logs in(then we generate a token, and store it in browser, and this token will be used to access the website thoughout the permitted session), he will be able to access the website for all endpoints for a particular session. and when the session expires, the token will become invalid and user will need to re log in to get a new token.

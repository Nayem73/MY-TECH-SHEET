- created `ProfilePage.tsx` under the `pages` section so that I can put the `ChangePasswordForm.tsx` component in it and test it from the `/profile` route

- to include `/profile` in routing I did the following changes:

```ts
const App = () => {
    return (
        <>
            <CssBaseline />
            <Router>
                <Routes>
                    <Route path="/" element={<SignInPage />} />
                    <Route path="/profile" element={<ProfilePage />} />
                </Routes>
            </Router>
        </>
    );
};
```

# **ChangePasswordForm.tsx** details:

- used `useState` hook to manage form input values (`oldPassword` and `newPassword`), visibility states for the passwords, loading state for the submit button, and error messages for form validation.

- used these from the @mui/material:
  
  -     Button,
    
        TextField,
    
        InputAdornment,
    
        IconButton,
    
        Box,
    
        Typography,
    
        Container,
    
        CircularProgress,
        Visibility, VisibilityOff  from @mui/icons-material
        

- **Validation Function**: This function validates the passwords:
  
  - Checks if the fields are empty.
  - Ensures the new password is not the same as the old password.
  - Checks the length of the new password.
  - Ensures the new password meets the complexity requirements (uppercase, lowercase, number, and symbol).
  - please check if the regex is correct (both chatGPT and MS Copilot said it's correct for above conditions): passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$/

- timeout set for handlesubmit is 2000 ms

- kept the form layout similar to Pallob san's signin component

- can toggle between text and password by clicking on mui icon visibility/off and useState hook is used for such state changes.

- for validation, if error is true then shows the helperText. Code and functionality taken from mui

- These are the error messages added after validation fails:
  
  - if form field is empty: "This field cannot be empty."
  
  - oldPassword === newPassword: "Old password and new password cannot be the same."
  
  - newPassword.length < 8 || newPassword.length > 20 : "Password must contain at least 8 characters and at most 20 characters."
  
  - if !passwordRegex.test(newPassword) : "Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 symbol."

- If Change Password button is pressed then loading is true and CircularProgress size={24} from mui is used for loading, timeout is set to 2000ms.

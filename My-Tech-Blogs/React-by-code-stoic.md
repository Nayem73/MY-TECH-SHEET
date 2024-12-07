#### Create React App using Vite

```jsx
npm create vite@4.1.0
npm install
npm run dev
```

- React is called a single page application. In the entire project structure of React, we only have one html file called `index.html`

![](assets/2024-12-07-10-36-04-image.png)



### why do we use components in React?

components are reusable. We should break down the user interface to multiple smaller UI components. Because:

- **modularity of code:** using components make the application modular such that you have multiple modules or sections inside of your application. Each component acts like a module and provides specific UI functionality each. Managing such applications is easy.  

- **reusability:** Once you make a component, you can reuse it anwhere.

- **Testing:** Because the components are isolated from one another, that means, one componsent is not dependent on another component, it becomes easier to test them individually. So we can ensure that each component works well. So, if we ensure that every single component works well, that means our entire react application is going to work fine.

- **Abstraction:** By using components we can achieve abstraction by hiding away the details of implementation



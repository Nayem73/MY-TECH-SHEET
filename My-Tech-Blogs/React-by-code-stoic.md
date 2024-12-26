#### Create React App using Vite

```jsx
npm create vite@4.1.0
npm install
npm run dev
```

- React is called a single page application. In the entire project structure of React, we only have one html file called `index.html`

![](assets/2024-12-07-10-36-04-image.png)

### why do we use components in React?

A component in Javascript is nothing but a function that returns jsx

components are reusable. We should break down the user interface to multiple smaller UI components. Because:

- **modularity of code:** using components make the application modular such that you have multiple modules or sections inside of your application. Each component acts like a module and provides specific UI functionality each. Managing such applications is easy.  

- **reusability:** Once you make a component, you can reuse it anwhere.

- **Testing:** Because the components are isolated from one another, that means, one componsent is not dependent on another component, it becomes easier to test them individually. So we can ensure that each component works well. So, if we ensure that every single component works well, that means our entire react application is going to work fine.

- **Abstraction:** By using components we can achieve abstraction by hiding away the details of implementation

### learnt about arrays in javascript and how to access each element of an array using map. map needs to have a unique key as well. so you need to assign a unique key during accessing the elements of array. an array could be an array of objects as well. you can also pass arrays or objects or strings or numbers, literally anything through props from one component to other component

# UseState Hook

```jsx
import { useState } from "react";

export default function Count() {
  const [count, setCount] = useState(0);

  function increase() {
    setCount(count + 1);
  }

  function decrease() {
    setCount(count - 1);
  }

  return (
    <div>
      <h1>Current count is: {count}</h1>
      <button onClick={increase}>Increment</button>
      <button onClick={decrease}>Decrement</button>
    </div>
  );
}
```

# React input Form

- way-1:

```jsx
import { useState } from "react";

export default function () {
  const [name, setName] = useState("");
  function handleChange(event) {
    console.log(event.target.value);
    console.log(event);
    setName(event.target.value);
  }

  return (
    <div>
      <form>
        <input
          onChange={function temp(event) {
            return handleChange(event);
          }}
          type="text"
          value={name}
        />
      </form>
    </div>
  );
}
```

- way 2:

```jsx
import { useState } from "react";

export default function () {
  const [name, setName] = useState("");
  function handleChange(event) {
    console.log(event.target.value);
    console.log(event);
    setName(event.target.value);
  }

  return (
    <div>
      <form>
        <input onChange={handleChange} type="text" value={name} />
      </form>
    </div>
  );
}
```

- way 3:

```jsx
import { useState } from "react";

export default function () {
  const [name, setName] = useState("");
  function handleChange(event) {
    console.log(event.target.value);
    console.log(event);
    setName(event.target.value);
  }

  return (
    <div>
      <form>
        <input
          onChange={(event) => handleChange(event)}
          type="text"
          value={name}
        />
      </form>
    </div>
  );
}
```

- way 4:

```jsx
import { useState } from "react";

export default function () {
  const [name, setName] = useState("");

  return (
    <div>
      <form>
        <input
          onChange={(event) => setName(event.target.value)}
          type="text"
          value={name}
        />
      </form>
    </div>
  );
}
```

# Arrow Function

Dear Sir/Madam,

I am writing as a follow-up to my previous email regarding the corrections needed for the "**Itinerary with Information (滞在予定表)**" and "**Flight Itinerary Issued by Travel Agency or Airline Office (予約確認書)**" forms.

In my earlier email, I mentioned that the departure point in the "**Itinerary with Information (滞在予定表)**" form is incorrectly listed as Bole International Airport and Dubai International Airport. However, it should be **Hazrat Shahjalal International Airport in Dhaka, Bangladesh.**

Additionally, I have noticed another issue in the same "**Itinerary with Information (滞在予定表)**" form. The departure date from Japan after the internship is currently listed as **14th February**, but I believe it should be **24th February.**

I would be grateful if you could review these points and make the necessary corrections. Please let me know if you require any additional information or documents from my side to resolve these matters.

Thank you for your attention and continued support. I look forward to hearing from you.

Sincerely,  
Nayem Mehedi

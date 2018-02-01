# Coediting-by-Socket

Provided simultaneously editing function as Google-Doc. Using socket to avoid polling overhead.

### Demo
[Link](https://shielded-scrubland-76433.herokuapp.com/)

### Todo:

- Add locking mechanism (maybe optimistic one?) to prevent racing condition when both clients emit editing in a short time frame.

- Use self-defined /div section instead of /textarea to provide flexiblility. e.g. keep cursor at different place for each clients.

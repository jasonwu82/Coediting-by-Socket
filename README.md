# Coediting-by-Socket

Provided simultaneously editing function as Google-Doc. Using socket to avoid polling overhead.

Use Redis as backend volatile datastore.

### Demo

[Link](https://shielded-scrubland-76433.herokuapp.com/)

Use $ROOT_URL/($ROOM_ID) to enter different room where each room has separated channel.

(such as [$ROOT_URL/room1](https://shielded-scrubland-76433.herokuapp.com/room1))

### Todo:

- Add locking mechanism (maybe optimistic one?) to prevent racing condition when both clients emit editing in a short time frame.

- Use self-defined /div section instead of /textarea to provide flexiblility. e.g. keep cursor at different place for each clients.

- Provide non-volatile storage

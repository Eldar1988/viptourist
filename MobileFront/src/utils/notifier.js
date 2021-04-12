import {Notify} from "quasar"

export default function(message, color='dark', position='top') {
  Notify.create({
    message: message,
    color: color,
    position: position,
    actions: [{color: 'white', icon: 'close'}]
  })
}

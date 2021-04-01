import {Notify} from 'quasar'

const notifier = (message, color='dark') => {
  Notify.create({
    message: message,
    color: color,
    position: 'top'
  })
}

export default notifier

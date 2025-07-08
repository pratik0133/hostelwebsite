from flask import Flask, render_template, request, redirect, url_for, flash
from room import rooms_list
app = Flask(__name__)
app.secret_key = '5d894a501c88fbe735c6ff496a6d3e51'


@app.route('/')
def home():
    return render_template('home.html', rooms=rooms_list)

@app.route('/rooms')
def rooms():
    return render_template('rooms.html', rooms=rooms_list)

@app.route('/booking')
def booking():
    room_id = request.args.get('room_id')
    selected_room = None
    if room_id:
        selected_room = next((r for r in rooms_list if r['id'] == int(room_id)), None)
    return render_template('booking.html', rooms=rooms_list, selected_room=selected_room)

@app.route('/book', methods=['POST'])
def book():
    room_id = request.form.get('room_id')
    checkin = request.form.get('checkin')
    checkout = request.form.get('checkout')
    guests = request.form.get('guests')
    guest_name = request.form.get('guest_name', '')
    
    room = next((r for r in rooms_list if r['id'] == int(room_id)), None)
    
    if room:
        flash(f'Booking confirmed! {guest_name}, your {room["name"]} is reserved from {checkin} to {checkout} for {guests} guests.', 'success')
    else:
        flash('Room not found!', 'error')
    
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html',rooms=rooms_list)

@app.route('/contacts')
def contact():
    return render_template('contacts.html',rooms=rooms_list)

if __name__ == '__main__':
    app.run(debug=True)
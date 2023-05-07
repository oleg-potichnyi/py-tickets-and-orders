from datetime import datetime

from typing import Optional

from django.db import transaction

from db.models import Order, Ticket


def create_order(
    tickets: list[dict], username: str, date: Optional[str] = None
) -> None:
    with transaction.atomic():
        order = Order(user=username)
        if date:
            order.created_at = datetime.strptime(date, "%Y-%m-%d %H:%M")
        order.save()
        for ticket_data in tickets:
            ticket = Ticket(
                order=order,
                row=ticket_data["row"],
                seat=ticket_data["seat"],
                movie_session=ticket_data["movie_session"],
                username=username,
            )
            ticket.save()


def get_orders(username: Optional[str] = None) -> None:
    all_orders = Order.objects.all()
    if username:
        all_orders = all_orders.filter(user__username=username)
    return all_orders
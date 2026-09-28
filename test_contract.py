import pytest
from contract import AgentServiceEscrow


def test_create_escrow():
    contract = AgentServiceEscrow()
    escrow = contract.create_escrow(
        escrow_id="escrow-001",
        buyer_agent="Agent_A",
        seller_agent="Agent_B",
        amount=100.0,
        service_spec="Analyze market sentiment data."
    )
    assert escrow["status"] == "LOCKED"
    assert escrow["amount"] == 100.0
    assert "escrow-001" in contract.escrows


def test_submit_deliverable_and_settle():
    contract = AgentServiceEscrow()
    contract.create_escrow(
        escrow_id="escrow-002",
        buyer_agent="Agent_A",
        seller_agent="Agent_B",
        amount=500.0,
        service_spec="Generate Python script for automated web scraping."
    )

    result = contract.submit_deliverable_and_settle(
        escrow_id="escrow-002",
        deliverable_url="https://api.example.com/delivery/script.py"
    )

    assert result["status"] == "RELEASED"
    assert result["deliverable_url"] == "https://api.example.com/delivery/script.py"


def test_get_escrow_details():
    contract = AgentServiceEscrow()
    contract.create_escrow(
        escrow_id="escrow-003",
        buyer_agent="Agent_X",
        seller_agent="Agent_Y",
        amount=200.0,
        service_spec="Translation service."
    )

    details = contract.get_escrow_details("escrow-003")
    assert details["buyer_agent"] == "Agent_X"

    not_found = contract.get_escrow_details("non-existent")
    assert not_found["status"] == "NOT_FOUND"

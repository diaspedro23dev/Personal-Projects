/// <reference types="cypress"/>

const { should } = require("chai")

describe("Teste de api dos Correios", () => {
    it.only("Casa no Rio", () => {
        cy.request({
            url: 'https://viacep.com.br/ws/23078110/json/',
            method: 'GET',
            log: true,
            failOnStatusCode: true,
            encoding: 'utf8'
        }).should((response) => {
            expect(response.status).to.eq(200)
            expect(response.statusText).to.eq("OK")
            expect(response.isOkStatusCode).to.eq(true)
            should(response).have.property('cep')
        })
        
    })
})